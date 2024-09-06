```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Sortedd list according to criteria above
    """
    if not nums:
        return []
    summed_nums = [sum(map(int, str(num))) for num in nums]
    sorted_nums = sorted(summed_nums)
    return [nums[i] for i in range(len(nums)) if summed_nums[i] == sorted_nums[i]]
```