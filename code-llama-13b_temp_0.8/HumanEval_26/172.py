from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # bool_list = [True] * len(numbers)
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] == numbers[j]:
    #             bool_list[j] = False
    # new_list = []
    # for i in range(len(bool_list)):
    #     if bool_list[i]:
    #         new_list.append(numbers[i])
    # return new_list
    # numbers.sort()
    # for i in range(len(numbers) - 1, 0, -1):
    #     if numbers[i] == numbers[i - 1]:
    #         numbers.pop(i)
    # return numbers
    new_list = []
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list

