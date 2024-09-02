from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Check if numbers is empty or not
    if len(numbers) == 0:
        return []

    # Initialize output list with first element of numbers
    output = [numbers[0]]

    # Loop through remaining elements of numbers
    for i in range(1, len(numbers)):
        output.append(delimeter)
        output.append(numbers[i])

    return output

