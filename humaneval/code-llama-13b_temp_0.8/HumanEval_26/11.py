from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    hash_dict = {}
    for number in numbers:
        hash_dict[number] = hash_dict.get(number, 0) + 1
    return [k for k in hash_dict if hash_dict[k] == 1]

