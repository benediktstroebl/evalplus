from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dict of counts of each number in the list
    #
    # >>> counts = {1: 1, 2: 2, 3: 1, 4: 1}
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    # Filter the numbers that do not occur more than once.
    #
    # >>> numbers = [1, 3, 4]
    numbers = [n for n in numbers if counts[n] == 1]
    return numbers

