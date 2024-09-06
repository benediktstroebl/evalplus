from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # This way does not work - more info in notes.md
    # return list(dict.fromkeys(numbers))
    # It works, but the result is not sorted
    # return list(set(numbers))
    # This way works, but it is not as simple as using a dictionary
    result: List[int] = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result
