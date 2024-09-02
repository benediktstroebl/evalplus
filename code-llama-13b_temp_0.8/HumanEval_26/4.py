from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Can be done in one pass over the list:
    # (1) iterate over the list
    # (2) check if the element occurs in the list before the current index
    #     if it does, remove the current element.
    # (3) otherwise, continue

    # 1
    for i in range(len(numbers)):
        # 2
        for j in range(i + 1, len(numbers)):
            # 3
            if numbers[i] == numbers[j]:
                numbers.remove(numbers[i])

    return numbers

