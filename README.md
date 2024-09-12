# Тестирование GitHub API с использованием PyTest


Этот проект содержит набор тестов для взаимодействия с GitHub API с использованием PyTest. Тесты охватывают создание, проверку, поиск и удаление репозитория на GitHub.

## Описание проекта
Проект состоит из нескольких тестов, которые проверяют основные операции с репозиториями на GitHub:

Создание репозитория: Тест проверяет возможность создания нового репозитория.

Проверка создания репозитория: Тест проверяет, что созданный репозиторий существует.

Поиск репозитория в списке: Тест проверяет, что созданный репозиторий присутствует в списке всех репозиториев пользователя.

Удаление репозитория: Тест проверяет возможность удаления репозитория.

## Установка
Клонируйте репозиторий:

git clone https://github.com/Rufatello/qit_api.git

### Установите необходимые зависимости:

pip install -r requirements.txt
#### Использование
Создайте файл .env в корне проекта и добавьте в него следующие переменные окружения:

GITHUB_TOKEN=your_github_token

GITHUB_API_URL=https://api.github.com

owner=your_github_username

##### Запустите тесты:
1 - Откройте терминал или командную строку

2 - Перейдите в директорию проекта, если вы еще не там

3 - Запустите тесты с помощью команды pytest


Переменные окружения
Для корректной работы тестов необходимо настроить следующие переменные окружения:

GITHUB_TOKEN: Ваш токен доступа к GitHub API.

GITHUB_API_URL: URL для работы с GitHub API (по умолчанию https://api.github.com).

owner: Имя пользователя GitHub.
