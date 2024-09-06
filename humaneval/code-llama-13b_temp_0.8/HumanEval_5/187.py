from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []

    # intersperse is called with an empty list, nothing to do
    if not numbers:
        return result

    # intersperse is called with a list of 1 element
    if len(numbers) == 1:
        return [numbers[0]]

    # Append the first number of the list to the result
    result.append(numbers[0])

    for number in numbers[1:]:
        # Insert the delimeter between two numbers in the list
        result.append(delimeter)

        # Append the next number in the list to the result
        result.append(number)

    return result

