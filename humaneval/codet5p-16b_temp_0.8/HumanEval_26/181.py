from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if numbers:
        duplicate_set = set()
        non_duplicate_list = []
        for i in range(0, len(numbers)):
            if numbers[i] not in duplicate_set:
                non_duplicate_list.append(numbers[i])
                duplicate_set.add(numbers[i])

        return non_duplicate_list
    else:
        return []

