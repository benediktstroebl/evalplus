from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return numbers

    # Pop the first element from the list and put it in a temporary list
    numbers_copy = numbers.pop(0)

    # Repeatedly add elements to the temporary list, unless the element is already
    # present in the temporary list
    for number in numbers:
        if number != numbers_copy:
            numbers_copy.append(number)

    # Return the temporary list
    return numbers_copy

