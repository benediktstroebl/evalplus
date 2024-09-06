from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # pylint: disable=no-else-return
    if len(numbers) <= 1:
        return numbers
    else:
        numbers_to_keep = [numbers[0]]
        for number in numbers[1:]:
            if number not in numbers_to_keep:
                numbers_to_keep.append(number)
        return numbers_to_keep
