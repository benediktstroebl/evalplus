```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if ind == sorted(range(len(nums)), key=lambda x: (sum(map(int, str(nums[x]))), x))][0]
    return [num for num in nums if num == sorted_nums][0]
```

This code block implements the `order_by_points` function, which sorts the list of integers `nums` based on the sum of their digits, and if there's a tie, it sorts based on their index in the original list. The output is the list sorted in ascending order.