from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) == 0:
        return []
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    result = []
    for number, count in count.items():
        if count == 1:
            result.append(number)
    return result

