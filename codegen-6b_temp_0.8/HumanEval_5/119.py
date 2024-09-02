from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # first_delimeter = delimeter
    # last_delimeter = delimeter

    # first_delimeter_idx = 0
    # last_delimeter_idx = len(numbers) - 1

    # for idx, num in enumerate(numbers):
    #     if idx == 0:
    #         numbers[0] = first_delimeter
    #     elif idx == last_delimeter_idx:
    #         numbers[last_delimeter_idx] = last_delimeter
    #     else:
    #         numbers[idx] = first_delimeter

    # return numbers

    # Another way
    # prev_num = delimeter
    # numbers_len = len(numbers)
    # for idx, num in enumerate(numbers):
    #     if idx == 0:
    #         numbers[0] = prev_num
    #     elif idx == numbers_len - 1:
    #         numbers[-1] = prev_num
    #     else:
    #         numbers[idx] = prev_num
    #         prev_num = delimeter

    # return numbers

    # Another way
    # prev_num = delimeter
    # num_array = []
    # for idx, num in enumerate(numbers):
    #     if idx == 0:
    #         num_array.append(prev_num)
    #     elif idx == len(numbers) - 1:
    #         num_array.append(prev_num)
    #     else:
    #         num_array.append(delimeter)
    #         prev_num = num

    # return num_array

    # another way
    # prev_num = delimeter
    # num_array = []
    # for idx, num in enumerate(numbers):
    #     if idx == 0:
    #         num_array.append(prev_num)
    #     elif idx == len(numbers) - 1:
    #         num_array.append(prev_num)
    #     else:
    #         num_array.