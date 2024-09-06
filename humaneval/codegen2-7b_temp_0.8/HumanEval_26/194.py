from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    dupes = {}
    new_list = []
    for number in numbers:
        if number not in dupes:
            new_list.append(number)
            dupes[number] = 1
        else:
            dupes[number] += 1
    return new_
