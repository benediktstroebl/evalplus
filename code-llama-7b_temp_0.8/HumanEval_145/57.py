
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
    list_with_sum = []
    for i in range(len(nums)):
        num = nums[i]
        num_str = str(num)
        sum_of_num = 0
        for ch in num_str:
            sum_of_num += int(ch)
        list_with_sum.append((sum_of_num, i, num))
    list_with_sum.sort()
    ordered_list = []
    for sum_of_num, i, num in list_with_sum:
        ordered_list.append(num)
    return ordered_list

