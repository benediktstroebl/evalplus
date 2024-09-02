from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # as a general rule, "if you don't know what to do,
    #   use the highest-level functions available to you"
    # the `.sort()` method alters the original list, but in-place,
    #   so we can't really use it for anything useful
    # so we'll make a copy and sort that instead
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    # this will hold our filtered list
    result = []
    # will hold the last element we've seen
    # (None is the identity value for `is` and `is not`,
    #   so it's a safe value to initialize it to)
    last_element = None

    for element in numbers_copy:
        # if this is the first time we've seen this element,
        #   or the last element we saw was different from this one,
        #   append this element to the result list
        if last_element is None or last_element is not element:
            result.append(element)
            # set the last element to the current one
            last_element = element

    return result

