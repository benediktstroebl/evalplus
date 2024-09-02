from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return numbers
    elif len(numbers) == 1:
        return numbers
    else:
        last_num = numbers[0]
        index = 1
        while index < len(numbers):
            if numbers[index] == last_num:
                del numbers[index]
            else:
                last_num = numbers[index]
                index += 1
    return numbers

