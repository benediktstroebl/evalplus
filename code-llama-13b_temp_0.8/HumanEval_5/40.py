from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []

    # keep track of previous element of input list
    previous_element = None

    for element in numbers:
        # for very first iteration, there is no previous element
        # so don't insert delimeter between first element and itself
        if previous_element is not None:
            result.append(delimeter)

        # append current element to result
        result.append(element)

        # now current element becomes previous element for next iteration
        previous_element = element

    return result

