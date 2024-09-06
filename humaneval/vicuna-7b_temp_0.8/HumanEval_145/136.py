
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
    # check if there is a number
    if not nums:
        return []

    # sort the list and get the sum of digits
    nums_sorted = sorted(nums)
    digits_sum = reduce(lambda x, y: x + int(y), nums_sorted)

    # sort the list again but only within the range of digits_sum
    nums_sorted_again = sorted(nums, key=lambda x: digits_sum - int(str(x)))

    # return the sorted list
    return nums_sorted_again
