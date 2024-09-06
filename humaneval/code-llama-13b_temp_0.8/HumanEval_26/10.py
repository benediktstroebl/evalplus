from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    unique_numbers = set()
    unique_list = []
    for n in numbers:
        if n not in unique_numbers:
            unique_numbers.add(n)
            unique_list.append(n)
    return unique_list

