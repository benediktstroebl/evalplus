```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no guaranteed order.

    Returns:
        list: Ordered list according to criteria above.
    """
    if not nums:
        return []

    # Track the sorted list in descending order by sum of digits and original index.
    sorted_idx = sorted(range(len(nums)), key=lambda idx: (len(str(nums[idx])) - sum(int(d) for d in str(nums[idx])), idx))
    # Reverse the order to sort in ascending order.
    return [nums[i] for i in sorted_idx[::-1]]
```

This script provides a function `order_by_points` that takes in a list of integers (`nums`) and returns a list ordered according to the specified criteria. The function first checks if the input list is empty, returning an empty list itself if so. It then uses a sorted index list to track descending order based on the sum of digits and original index, and reverses this order to achieve ascending sorting.