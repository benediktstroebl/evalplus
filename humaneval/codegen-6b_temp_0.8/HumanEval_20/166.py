from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = list(sorted(numbers))
    num1 = numbers[0]
    num2 = numbers[1]
    if num1 - num2 > 0.999:
        num1, num2 = num2, num1
    guess1 = float(num1)
    guess2 = float(num2)
    while guess1 != num1 or guess2 != num2:
        if guess1 > num1:
            guess1 = float(guess1 - 0.5)
        else:
            guess1 = float(guess1 + 0.5)
        if guess2 > num2:
            guess2 = float(guess2 - 0.5)
        else:
            guess2 = float(guess2 + 0.5)
    return num1, num2

