from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # This should be a tail recursion
    def intersperse_helper(numbers: List[int], delimeter: int, idx: int, result: List[int]):
        if idx >= len(numbers):
            return result
        result.append(numbers[idx])
        if idx + 1 < len(numbers):
            result.append(delimeter)
        return intersperse_helper(numbers, delimeter, idx + 1, result)

    return intersperse_helper(numbers, delimeter, 0, [])

