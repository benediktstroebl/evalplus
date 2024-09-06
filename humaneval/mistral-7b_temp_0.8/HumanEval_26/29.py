from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    num_counts = {}
    for number in numbers:
        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1

    return [number for number, count in num_counts.items() if count == 1]

