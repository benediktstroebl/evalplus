from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if numbers is None:
        raise ValueError
    elif len(numbers) == 0:
        return numbers
    else:
        result = [numbers[0]]
        for i in numbers[1:]:
            if i!= result[-1]:
                result.append(i)
    return result

