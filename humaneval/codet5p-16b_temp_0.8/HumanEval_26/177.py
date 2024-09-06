from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if not numbers:
        return numbers

    number_of_occurrences = {}
    result = []

    for number in numbers:
        if number in number_of_occurrences:
            number_of_occurrences[number] += 1
        else:
            number_of_occurrences[number] = 1
            result.append(number)

    return result
