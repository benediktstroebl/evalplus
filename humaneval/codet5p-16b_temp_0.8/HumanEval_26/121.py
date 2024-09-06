from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    duplicates_indices = []
    for index, element in enumerate(numbers):
        if index!= 0:
            if numbers[index] == numbers[index-1]:
                duplicates_indices.append(index)
    
    for index in sorted(duplicates_indices, reverse=True):
        numbers.pop(index)
    return numbers
    
    
