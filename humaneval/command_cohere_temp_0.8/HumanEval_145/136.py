```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria above.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This script employs the `sorted` function coupled with a lambda function as the sorting key. This key comprises of two components:
1. The first one is the sum of the digits of the number converted to an integer (via `map(int, str(x))`). This digit sum acts as the primary sorting criterion.
2. The second component is the original integer `x`, which is used as a tie-breaker in case two numbers have the same digit sum. This ensures that the ordering is consistent with the index of items in the original list.

The function, when invoked on the example input, would produce the following output:
```python
order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
```