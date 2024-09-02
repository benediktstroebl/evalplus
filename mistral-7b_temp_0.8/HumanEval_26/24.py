from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Solution #1
    # Set to keep track of the set of seen numbers
    seen_numbers = set()

    # Iterate over the numbers
    for number in numbers:
        if number not in seen_numbers:
            seen_numbers.add(number)

    # Convert the set into a list and return the list
    return list(seen_numbers)

    # Solution #2
    # List comprehension
    #return [number for number in numbers if number not in numbers]
