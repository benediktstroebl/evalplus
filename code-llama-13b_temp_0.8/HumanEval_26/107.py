from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    distinct_numbers = set()
    distinct_list = []
    for number in numbers:
        if number not in distinct_numbers:
            distinct_numbers.add(number)
            distinct_list.append(number)
    return distinct_list

