from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Your code here.
    # Think about the base case.
    # How can you extend the base case to reach the general case?
    if len(numbers) == 1:
        return numbers
    elif len(numbers) == 2:
        return numbers
    elif len(numbers) > 2:
        result = [numbers[0]]
        for i in range(1, len(numbers) - 1):
            result.append(numbers[i])
            result.append(delimeter)
        result.append(numbers[-1])
        return result

