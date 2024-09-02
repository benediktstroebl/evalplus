from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    dict_of_nums = {}
    for i in numbers:
        if i not in dict_of_nums:
            dict_of_nums[i] = 1
        else:
            dict_of_nums[i] += 1
    output = []
    for num in numbers:
        if dict_of_nums[num] <= 1:
            output.append(num)
            dict_of_nums[num] -= 1
    return output
