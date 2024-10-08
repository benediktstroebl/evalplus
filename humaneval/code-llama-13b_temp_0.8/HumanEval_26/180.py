from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # using a set 
    # return list(set(numbers))
    
    # using a dictionary
    numbers_dict = {}
    for num in numbers:
        if num not in numbers_dict:
            numbers_dict[num] = 1
        else:
            numbers_dict[num] += 1
    return [key for key, value in numbers_dict.items() if value == 1]
