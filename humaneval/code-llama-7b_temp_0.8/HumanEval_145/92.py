
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # [5, 11, 5, 1111, 111, 1111111111, 1111, 111111111, 111111111111111111111, 11111, 111111111111111111111111111, 1111111111111111111111111, 1111111111111111111111111111, 11111111111111111111111111111]
    # [1, 2, 1, 3, 4, 15, 3, 5, 30, 6, 35, 7, 36, 8, 37, 9, 38]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    nums_index = []
    nums_sum = []
    nums_index_sum = []
    for index, num in enumerate(nums):
        nums_index.append(num)
        nums_sum.append(sum_of_digits(num))
        nums_index_sum.append((num, index, nums_sum[-1]))
    # print(nums_index_sum)

    result = []
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # [1, 2, 3, 4, 5, 6, 
