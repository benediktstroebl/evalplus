
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
    # sort the list
    nums.sort()

    # keep track of the sum of digits for the first num in the list
    prev_sum = nums[0]
    for num in nums[1:]:
        # add the digits of the current number and update the sum
        prev_sum = (prev_sum + num) % 10

    # return the list with the sorted numbers
    return [num for num in nums if prev_sum == (num // 10) % 10]
