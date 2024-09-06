from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # 1. Pomyśl o rozwiązaniu problemu z wykorzystaniem wbudowanej funkcji max
    # 2. Przetestuj poprawność algorytmu
    # 3. Przetestuj skuteczność algorytmu na dużych danych
    result = []
    rolling_max_number = 0

    for number in numbers:
        if number > rolling_max_number:
            rolling_max_number = number
        result.append(rolling_max_number)
    return result

