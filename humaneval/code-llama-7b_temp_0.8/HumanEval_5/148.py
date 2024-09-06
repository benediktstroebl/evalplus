from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Check if the list is empty, if it is return an empty list
    if not numbers:
        return []

    # Create a new list of length one more than the input list
    new_list = [None] * (len(numbers) * 2 - 1)

    # Start index from 0
    i = 0
    # insert the first element
    new_list[i] = numbers[0]

    for j in range(1, len(numbers)):
        # insert the delimeter at current index
        new_list[i + 1] = delimeter
        # increment index by two to account for the inserted delimeter
        i += 2
        # insert the next element
        new_list[i] = numbers[j]

    return new_list

