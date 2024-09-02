
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

    my_list = []
    for i in nums:
        digit_sum = sum([int(k) for k in str(i)])
        my_list.append((digit_sum, i))
    sorted_list = sorted(my_list)
    new_list = []
    for i in sorted_list:
        new_list.append(i[1])
    return new_list

