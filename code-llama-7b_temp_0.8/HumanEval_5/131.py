from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if not numbers:
        return []

    # initialize list with a first element
    new_numbers = [numbers[0]]

    for index, element in enumerate(numbers):
        # if we're at the last element
        if index == len(numbers) - 1:
            # add it to the end of the list
            new_numbers.append(element)
            break

        # insert 'delimeter' between the current and next element
        new_numbers.append(delimeter)
        new_numbers.append(element)

    return new_numbers
