from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = []
    index = 0
    while index < len(numbers):
        num = numbers[index]
        if num not in numbers[index+1:]:
            result.append(num)
        index = index + 1
    return result

