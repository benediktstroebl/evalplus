from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if not numbers:
        return []

    delimeters = len(numbers) - 1
    interspersed_list = [0] * (len(numbers) + delimeters)

    write_index = 0
    for read_index, number in enumerate(numbers):
        interspersed_list[write_index] = number
        if read_index != len(numbers) - 1:
            write_index += 1
            interspersed_list[write_index] = delimeter
            write_index += 1

    return interspersed_list

