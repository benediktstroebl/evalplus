from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # This creates a list of the counts for each element. This uses
    # a defaultdict, which returns 0 for any item not in the dict.
    counts = {item: numbers.count(item) for item in set(numbers)}
    # Now we only keep items with a count of 1.
    return [item for item in numbers if counts[item] == 1]
