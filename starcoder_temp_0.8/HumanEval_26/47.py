from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # [1, 2, 3, 2, 4]
    # [1, 2, 3]
    # [1, 2, 3]
    # [1, 3]
    # [1, 3]
    # [1, 3, 4]
    # [1, 3, 4]
    # [1, 4]
    # [1, 4]
    # [1, 4]

    # For each number in numbers
    for i in range(len(numbers)):
        number = numbers[i]

        # If number occurs more than once
        if numbers.count(number) > 1:
            # Remove all occurences of number
            while numbers.count(number) > 1:
                numbers.remove(number)

    return numbers

