from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Step 1: Create an empty list
    interspersed_numbers = []

    # Step 2: Iterate over input list `numbers' and append each number to `interspersed_numbers' list
    for number in numbers:
        interspersed_numbers.append(number)

    # Step 3: Iterate over `interspersed_numbers' list and insert delimeter between every two consecutive numbers
    for i in range(len(interspersed_numbers) - 1):
        interspersed_numbers.insert(i + 1, delimeter)

    return interspersed_numbers
