from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    dict_of_numbers = {}
    for i in range(len(numbers)):
        if numbers[i] not in dict_of_numbers:
            dict_of_numbers[numbers[i]] = []
        dict_of_numbers[numbers[i]].append(i)

    for list_of_numbers in dict_of_numbers.values():
        if len(list_of_numbers) > 1:
            for i in range(len(list_of_numbers)):
                for j in range(i + 1):
                    if j > 0 and abs(list_of_numbers[i] - list_of_numbers[j]) < threshold:
                        return True

    return False

