```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This script uses the `sorted` function and a lambda function as the sorting key to achieve the desired ordering. It first sorts the list based on the sum of digits, and if there's a tie, it uses the index as a tiebreaker to maintain the original order of equal elements.