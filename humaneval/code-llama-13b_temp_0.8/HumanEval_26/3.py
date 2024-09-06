from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count = 0
    while count < len(numbers):
        item = numbers[count]
        count2 = count + 1
        while count2 < len(numbers):
            if item == numbers[count2]:
                del numbers[count2]
            else:
                count2 += 1
        count += 1
    return numbers
