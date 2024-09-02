from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Find first occurence of any number that repeats and remove all from there
    # onwards
    last_occurrence_of_each = {number: i for i, number in enumerate(numbers)}
    sorted_numbers = sorted(last_occurrence_of_each.items(),
                            key=lambda pair: pair[1])
    start_indexes = {number: index for index, (number, _) in enumerate(sorted_numbers)}

    for (number, _) in sorted_numbers:
        if number == sorted_numbers[start_indexes[number]][0]:
            continue
        numbers[start_indexes[number]] = sorted_numbers[start_indexes[number]][0]

    return numbers

