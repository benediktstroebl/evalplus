from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if numbers == []:
        return numbers
    current = numbers[0]
    duplicates = []
    unique = [numbers[0]]
    for number in numbers:
        if number == current:
            duplicates.append(number)
        else:
            current = number
            unique.append(number)
    return unique + list(set(duplicates))

