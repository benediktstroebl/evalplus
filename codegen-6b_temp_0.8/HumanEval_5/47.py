from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    pos = 0
    n = len(numbers)
    newlist = []

    if n % 2 == 0:
        last = n - 1
        second_last = n - 2
        while pos <= last:
            newlist.append(numbers[pos])
            if pos < last:
                newlist.append(delimeter)
            pos += 1
        pos = 0
        while pos < second_last:
            newlist.append(numbers[pos])
            if pos < second_last:
                newlist.append(delimeter)
            pos += 1
    else:
        last = n - 1
        second_last = n - 1
        d = delimeter
        while pos <= last:
            newlist.append(numbers[pos])
            if pos < last:
                newlist.append(d)
            pos += 1
        pos = 0
        while pos < second_last:
            newlist.append(numbers[pos])
            if pos < second_last:
                newlist.append(d)
            pos += 1

    return newlist

