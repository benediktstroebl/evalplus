
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
    nums = sorted(nums)
    # keep track of the sum of the digits
    running_sum = 0
    # loop through the sorted list
    for i, n in enumerate(nums):
        # add the value of n to the sum of the digits
        running_sum += n
        # check if the sum of the digits is smaller than the current running sum
        # if so, subtract the sum of the digits from the running sum
        if running_sum < 10 * i:
            running_sum -= running_sum % 10
        # check if the sum of the digits is equal to the current running sum
        # if so, update the current running sum to the value of n
        elif running_sum == 10 * i:
            running_sum = n
    return nums
