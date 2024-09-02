
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
    # sort the list by sum of digits
    nums = sorted(nums, key=lambda x: sum(map(int, str(x))))
    
    # if the list is empty, return an empty list
    if not nums:
        return []
    
    # if there is only one item in the list, return it
    if len(nums) == 1:
        return [nums[0]]
    
    # if there are more than one item, return them sorted by their index in the original list
    return [nums.index(num) for num in nums]
