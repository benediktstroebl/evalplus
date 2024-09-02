from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Убедитесь, что список не пустой
    assert numbers, 'The given list should not be empty'

    # Створить перемінну с варіантом значення, Для визначенея за винятком залежностей от неї
    # одного из символів, за допомогою аргумента при запуску функції, тип запарами у list Элементы ітерабельно,
    # в тому числе символи
    prev_num = numbers[0]
    # Створити перемінну, яка вимикає нове значення
    is_close_prev = False
    # Створити перемінну, яка вимикає двого і більше значення
    is_more_than_two_prev = False

    for next_num in numbers:
        # Перевірити, чи нове значення залежає від попередні�