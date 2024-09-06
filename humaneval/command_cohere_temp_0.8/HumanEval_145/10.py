```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria above.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This script uses the `sorted` function, utilizing a custom key via the `lambda` syntax to sort the list according to the specified criteria. The key is a tuple, where the first element is the sum of digits of the number converted to a string, and the second element is the original number, serving as a tiebreaker in case two numbers have the same digit sum. The function then returns the ordered list.