import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()  # загрузка переменных окружения из файла .env
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # токен для гитхаб
GITHUB_API_URL = os.getenv('GITHUB_API_URL')  # адрес для работы
owner = os.getenv('owner')  # владелец


@pytest.fixture
def github_api():
    '''фикстура для создания заголовка запросов'''
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }
    return headers


@pytest.fixture
def repo_name():
    '''фикстура для имени репризитория'''
    return 'test_repo'


def test_github_repo_operations(github_api, repo_name):
    '''тест для создания репризитория'''
    create_repo_url = f'{GITHUB_API_URL}/user/repos'
    create_repo_data = {
        'name': repo_name,
        'auto_init': True
    }
    response = requests.post(create_repo_url, headers=github_api, json=create_repo_data)
    assert response.status_code == 201


def test_create_repo(github_api, repo_name):
    '''тест для проверки создания репризитория'''
    create_repo = f'{GITHUB_API_URL}/repos/{owner}/{repo_name}'
    responce = requests.get(create_repo, headers=github_api)
    assert responce.status_code == 200


def test_list_all_repositories(github_api, repo_name):
    '''тест для поиска в списке репризиториев '''
    list_repos_url = f'{GITHUB_API_URL}/user/repos'
    response = requests.get(list_repos_url, headers=github_api)
    assert response.status_code == 200

    repositories = response.json()
    repo_found = False
    for repo in repositories:
        if repo['name'] == repo_name:
            repo_found = True
            break
    assert repo_found, f'Repository {repo_name} not found in the list of repositories'


def test_delete_repo(github_api, repo_name):
    '''тест для удаления репризитория'''
    delete_repo_url = f'{GITHUB_API_URL}/repos/{owner}/{repo_name}'
    response = requests.delete(delete_repo_url, headers=github_api)
    assert response.status_code == 204
