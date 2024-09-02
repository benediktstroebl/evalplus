from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) < 2:
        return numbers

    # create a dictionary with numbers as keys, with values = 0
    dict_unique_numbers = {number: 0 for number in numbers}

    # replace key values with 1 if keys already exists
    for number in numbers:
        if dict_unique_numbers.get(number):
            dict_unique_numbers[number] += 1

    # return only keys with values = 0
    return [number for number in dict_unique_numbers.keys() if dict_unique_numbers[number] == 0]

