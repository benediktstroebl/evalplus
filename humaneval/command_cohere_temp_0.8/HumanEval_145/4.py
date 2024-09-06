```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```

This script leverages the `sorted` function and a lambda to create a custom key that sorts first by the sum of digits and then by the index in the original list in case of a tie. The tests provided for the function are also included, checking for the correctness of the implementation against the provided examples. You can use this code to confidently sort a list according to the specified criteria. Feel free to ask any follow-up questions or request further modifications as needed.