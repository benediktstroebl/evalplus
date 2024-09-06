from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a lookup dictionary
    number_dict = {}
    for num in numbers:
        number_dict[num] = number_dict.get(num, 0) + 1
    # Then go through the list again and add only the elements that
    # occur only once
    result = []
    for num in numbers:
        if number_dict[num] == 1:
            result.append(num)
    return result
