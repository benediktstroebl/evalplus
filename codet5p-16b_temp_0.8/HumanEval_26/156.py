from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return []
    else:
        return_list = [numbers[0]]
        for n in numbers[1:]:
            if n!= return_list[-1]:
                return_list.append(n)
        return return_list

