
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
    # sort the list in descending order of the sum of digits
    nums_rev = sorted(nums, key=lambda x: sum(map(int, x)))
    
    # for the first num, keep it as it is
    first_num = nums_rev[0]
    nums_rev = [first_num] + [num for num in nums_rev[1:] if num > first_num]
    
    return nums_rev