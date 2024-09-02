from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Uncomment and complete the following implementation
    # return sorted(set(numbers), key=numbers.index)
    # without using set or sorted
    seen = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
    return [num for num in numbers if num in seen]

