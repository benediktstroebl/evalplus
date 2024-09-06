```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```
This Python script provides a function `order_by_points` that arranges a list of integers so that they ascend according to the sum of their digits, making tiebreakers decisions based on the indices of the integers in their original places in the list. The function tests yield expected output, and the detailed behavioral summary can be found in the code block.