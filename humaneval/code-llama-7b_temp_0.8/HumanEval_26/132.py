from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return numbers

    last_value = numbers[0]
    result = [last_value]
    for index, value in enumerate(numbers[1:], start=1):
        if value != last_value:
            result.append(value)
            last_value = value

    return result

