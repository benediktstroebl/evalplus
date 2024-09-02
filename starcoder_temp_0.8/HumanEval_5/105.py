from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # If given an empty list, return an empty list
    if not numbers:
        return numbers

    # Otherwise, start with an empty list
    new_list: List[int] = []
    # Iterate over the numbers list
    for number in numbers:
        # Add the delimeter to the new list
        new_list.append(delimeter)
        # Add the number to the new list
        new_list.append(number)

    # Return the new list, minus the first delimeter
    return new_list[1:]
