from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # for i in range(len(numbers)):
    #     for j in range(len(numbers)):
    #         if numbers[i] == numbers[j]:
    #             continue
    #         if abs(numbers[i] - numbers[j]) < threshold:
    #             return True
    # return False
    #
    # for i in range(len(numbers)):
    #     if numbers.count(numbers[i]) > 1:
    #         return True
    # return False

    seen = []
    for n in numbers:
        if n in seen:
            return True
        seen.append(n)
    return False

