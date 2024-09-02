from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # solution with dictionary
    # seen_numbers = dict()
    # for i in numbers:
    #     if i not in seen_numbers:
    #         seen_numbers[i] = 1
    #     else:
    #         seen_numbers[i] += 1
    #
    # return [number for number in numbers if seen_numbers[number] == 1]

    # solution with set
    seen_numbers = set()
    return [x for x in numbers if not (x in seen_numbers or seen_numbers.add(x))]

