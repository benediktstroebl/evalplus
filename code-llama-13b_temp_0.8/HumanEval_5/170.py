from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) == 0:
        return []

    result = []
    # Iterate over the `numbers` list, starting from index 0
    for index, number in enumerate(numbers):
        result.append(number)
        # If the current index is not the last index of the `numbers` list
        if index != len(numbers) - 1:
            # Add the `delimeter` to the `result` list
            result.append(delimeter)

    return result

