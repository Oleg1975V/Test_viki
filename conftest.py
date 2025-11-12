import pytest


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура Pytest для инициализации и управления экземпляром WebDriver.

    Эта фикстура обеспечивает:
    - Создание нового экземпляра браузера Firefox для каждого теста
    - Настройку неявных ожиданий элементов
    - Автоматическое закрытие браузера после завершения теста

    Args:
        Нет параметров

    Yields:
        webdriver.Firefox: Экземпляр WebDriver для автоматизации браузера

    Examples:
        >>> def test_example(browser):
        ...     browser.get("https://example.com")
        ...     assert "Example" in browser.title

    Scope:
        function - фикстура создается заново для каждой тестовой функции
    """
    # Импорт внутри функции для избежания проблем с зависимостями
    from selenium import webdriver

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    # Установка неявного ожидания элементов (10 секунд)
    # WebDriver будет ожидать появления элементов перед выполнением операций
    driver.implicitly_wait(10)

    # Передача управления тестовой функции
    yield driver

    # Завершающие действия после теста - закрытие браузера
    driver.quit()
