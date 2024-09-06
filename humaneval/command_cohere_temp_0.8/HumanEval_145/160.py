```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Copy the list to preserve the original indices.
    sorted_nums = list(nums)
    
    # Sorting key function to determine sorting order.
    def sum_and_index(num):
        return (sum(int(d) for d in str(num)), nums.index(num))

    # Sort the list based on the sorting key function.
    sorted_nums.sort(key=sum_and_index)
    
    return sorted_nums
```

This code defines the `order_by_points` function, which takes a list of integers as input and sorts them according to the sum of their digits, breaking ties by using their index in the original list. The function then returns the sorted list of integers.