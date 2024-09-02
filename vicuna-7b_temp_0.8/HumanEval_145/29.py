
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
    # Use a variable to store the sum of digits of the last item
    # so that it can be used to determine the correct index of the last item
    # in the sorted list.
    last_sum = 0
    last_index = 0

    # Loop through the items in the list and update the sums and indices
    # of the items with the same sum of digits as the last item.
    for i in range(len(nums)):
        digit_sum = sum(int(num) for num in nums[:i+1])
        if last_sum == digit_sum:
            nums[i:last_index + 1], nums[last_index + 1:] = nums[last_index + 1:], nums[i+1:]
            last_index += 1
            last_sum = 0
        else:
            last_sum = digit_sum

    return nums