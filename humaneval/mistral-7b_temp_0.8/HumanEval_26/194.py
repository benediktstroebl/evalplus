from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # 1. add an empty list to keep track of seen values
    unique_numbers = []

    # 2. iterate through the list
    for number in numbers:
        # 3. if the number is not in the unique numbers, append it
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers

