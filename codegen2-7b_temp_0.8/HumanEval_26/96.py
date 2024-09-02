from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) == 0:
        return numbers

    last_number = numbers[0]
    new_list = []
    for num in numbers:
        if num!= last_number:
            new_list.append(num)
            last_number = num

    return new_
