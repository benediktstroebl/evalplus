
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
    # sort the list of integers
    nums = sorted(nums)

    # initialize variables to store the sum of digits of current number and current index of number in the sorted list
    current_sum = 0
    current_index = -1

    # iterate through the sorted list
    for i, num in enumerate(nums):
        current_sum = sum(num)
        if current_sum > 0:
            # if current sum is positive, move to the next element
            current_index += 1
            nums[i] = nums[current_index]
            current_index -= 1
        else:
            # if current sum is zero or less, use current number
            nums[i] = num

    return nums
