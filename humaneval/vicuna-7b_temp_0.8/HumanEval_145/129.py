
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
    n = len(nums)
    while n > 0:
        # Find the first non-positive number
        i = nums.index(nums.pop(0))
        while i > 0 and nums[i] < 0:
            i -= 1
        n -= i + 1
        # Append the non-positive number to the end of the sorted list
        nums.extend([nums[i] for i in range(i, n + 1) if nums[i] >= 0])
        # Sort the remaining numbers in ascending order
        nums = sorted(nums[i:n])

    return nums
