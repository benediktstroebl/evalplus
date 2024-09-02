
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
    # check if the input list is empty
    if not nums:
        return []

    # reverse the list since we want to sum the digits in descending order
    reversed_nums = sorted(nums[::-1], key=int)
    # add 1 to each element since the sum of digits is obtained by summing the absolute values of the digits
    nums_sum = [abs(sum(int(i) for i in str(n))) for n in reversed_nums]
    # sum the digits of the sum and take the first nums_sum[0] elements
    nums_sum_digit = sum(nums_sum)
    nums_digit = [num for num in reversed_nums if num < nums_sum_digit]
    return nums_digit

