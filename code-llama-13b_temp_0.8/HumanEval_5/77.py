from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Create empty list to store the output
    out = []

    # Loop through the numbers list
    for index, number in enumerate(numbers):

        # Check if the number is the last element in the list
        if index == len(numbers) - 1:

            # If it is the last element just append it to the out list
            out.append(number)
            continue

        # Append the current number to the out list
        out.append(number)

        # Append the delimeter number in between
        out.append(delimeter)

    return out

