from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    hash_table = {}
    for number in numbers:
        if number not in hash_table:
            hash_table[number] = 1
        else:
            hash_table[number] += 1
    return [item[0] for item in hash_table.items() if item[1] == 1]

