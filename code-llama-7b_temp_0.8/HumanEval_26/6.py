from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # This is the same as doing it in place, but with a marker at the end of
    # the list.
    if len(numbers) == 0:
        return []

    # This is a marker that tells us the last index where no duplicates have
    # been found.
    last_no_duplicate_index = 0
    for current_index in range(1, len(numbers)):
        current_number = numbers[current_index]
        last_number = numbers[last_no_duplicate_index]
        # If there are no duplicates of this number, add it to the list.
        if current_number != last_number:
            last_no_duplicate_index += 1
            numbers[last_no_duplicate_index] = current_number
    return numbers[:last_no_duplicate_index + 1]

