from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Fill in a code to make it work
    # Poor practice, but this is pythonic way to do it
    numbers = sorted(numbers)

    # Keeps track of last seen number
    last_number = numbers[0]
    result = []
    result.append(last_number)

    for i in range(1, len(numbers)):
        if numbers[i] != last_number:
            last_number = numbers[i]
            result.append(last_number)

    return result

