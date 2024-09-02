
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
    max_sum = 0
    for num in nums:
        sum = sum(int(d) for d in str(num))
        if sum > max_sum:
            max_sum = sum
        elif sum == max_sum and num[0] < 0:
            max_sum = sum
            max_index = 0
        else:
            max_index = 1
    return [num for num in nums if num[0] < 0 and num in [nums[i] for i in max_index..len(nums)]] + nums[max_index:]