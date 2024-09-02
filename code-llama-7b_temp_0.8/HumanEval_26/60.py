from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # The solution is pretty simple. We can iterate through the list,
    # keeping track of all the numbers that we have seen before.
    # If we have seen the number before, we don't add it to the solution.
    seen_numbers = set()
    solution = []
    for number in numbers:
        if number not in seen_numbers:
            seen_numbers.add(number)
            solution.append(number)

    return solution

