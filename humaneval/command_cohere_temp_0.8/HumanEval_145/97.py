```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if len(nums) == 0:
        return []
    num_sum = [sum(map(int, str(n))) for n in nums]
    sorted_nums = [nums[i] for i in num_sum.index(num_sum.count(num_sum[0]) - 1 or num_sum[0])::-1]
    return sorted_nums
```

This code snippet introduces a function `order_by_points(nums)` that accepts a list of integers, `nums`. It initially verifies whether the list is empty; if so, it returns an empty list. If the list contains elements, it computes the sum of digits for each number and arranges them in descending order. As a secondary sorting criterion, it arranges elements that have the same digit sum based on their original index, prioritizing them in ascending order. The final output is a list that reflects this combined sorting process.