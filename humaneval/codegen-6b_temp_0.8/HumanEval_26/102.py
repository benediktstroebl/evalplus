from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    last_seen = numbers[0]
    result = [last_seen]
    for number in numbers[1:]:
        if number != last_seen:
            result.append(number)
            last_seen = number
    return result

