
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
    # build a lookup table of sums for each number
    # (the index of the number is it's key in the table)
    sums = {}
    for index, num in enumerate(nums):
        sum = 0
        for digit in str(abs(num)):
            sum += int(digit)
        sums[index] = sum

    # sort the items by the sum, then by the index
    items = zip(sums.itervalues(), sums.iterkeys())
    items.sort()

    # re-order the items
    for index, (sum, key) in enumerate(items):
        nums[index] = nums[key]
    return nums

