from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # If no numbers were passed, return an empty list
    if not numbers:
        return []

    # Go through the list and keep track of the number of occurrences of each number
    # The output list will contain only the numbers that occur once.
    output = []
    last_seen = {}
    for num in numbers:
        if num not in last_seen:
            last_seen[num] = 1
            output.append(num)
        else:
            last_seen[num] += 1

    return output

