def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if ind == sorted(range(len(nums)), key=lambda x: (sum(map(int, str(nums[x]))), x))][0]
    return [num for num in nums if num == sorted_nums][0]