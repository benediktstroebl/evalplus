from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []

    # we need to keep track of what we have seen before
    seen_before = set()

    # this is our result list
    result = []

    for number in numbers:
        # we haven't seen this number before
        if number not in seen_before:
            # add it to the list
            result.append(number)

        # mark as seen
        seen_before.add(number)

    return result

