from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    print(f"Got the list {numbers}")
    if len(numbers) > 1:
        if numbers[0] == numbers[1]:
            return remove_duplicates(numbers[1:])
        else:
            return [numbers[0]] + remove_duplicates(numbers[1:])
    else:
        return numbers

