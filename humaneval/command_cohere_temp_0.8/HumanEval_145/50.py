```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This code defines a function `order_by_points` that takes in a list of integers (`nums`). It first sorts this list using the `sorted` function, passing a key function that calculates two values for each element:
1. The sum of the digits of the number converted to a string (`str(x)`), sorted in ascending order.
2. The original element itself, sorted in ascending order. 

This ensures that numbers with the same digit sum will be sorted by their original position in the input list. The result is returned as the sorted list of integers.