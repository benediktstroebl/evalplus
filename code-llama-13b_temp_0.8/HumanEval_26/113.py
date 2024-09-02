from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # numbers.sort()
    # result = list(numbers)
    # for i in range(len(numbers) - 1):
    #     if numbers[i] == numbers[i+1]:
    #         result.pop(i)
    # return result
    # return list(dict.fromkeys(numbers))
    # return list(set(numbers))
    my_dict = {}
    for num in numbers:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
    return [key for key, value in my_dict.items() if value == 1]

