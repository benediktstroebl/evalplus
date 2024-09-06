
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
    result = []
    for num in nums:
        # convert the number to string and sum of digits
        str_num = str(num)
        sum_digits = sum(int(d) for d in str_num)
        # sort the number according to the sum of digits
        sorted_num = sorted(str(num), key=lambda x: sum_digits - int(x))
        # convert the sorted string back to number and append to result
        result.append(int(sorted_num))
    return result
