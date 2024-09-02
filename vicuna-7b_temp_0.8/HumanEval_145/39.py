
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
    # faster_sort is a list of tuples containing the input list and the sum of digits
    # We keep the original list unchanged and return a copy of the list with the sorted items.
    faster_sort = [(nums, sum(int(n) for n in nums))]

    # Use heapsort for larger inputs
    if len(nums) >= 20:
        heapsort(faster_sort, 0)
        return list(faster_sort[-1][1])

    # Use insertion sort for smaller inputs
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] > nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums
