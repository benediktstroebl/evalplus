
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
        # for n = 0, the list is already sorted, so we return it
        if n == 0:
            return nums

        # for n > 0, find the smallest index of a negative number
        i = nums.index(0)
        while i != -1 and nums[i] > 0:
            i -= 1

        # sort the positive numbers to the right of the smallest negative number
        if i == -1:
            j = n - 1
        else:
            j = i
        nums[j:n] = sorted(nums[j:n])
        n -= 1

    return nums
