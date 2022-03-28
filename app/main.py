"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name (str): Имя пользователя

    Returns:
        str: Текст приветстви
    """
    return 'Привет, {name}'.format(name=name.title())
