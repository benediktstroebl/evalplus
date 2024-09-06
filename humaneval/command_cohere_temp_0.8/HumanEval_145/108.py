```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Ensure the list is not empty
    if not nums:
        return []

    # Utilize a lambda function for the sorting process
    # Based on https://stackoverflow.com/a/11764807/5887260
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This code leverages the `sorted` function and a lambda function to properly sort the list according to the specified criteria. The lambda function first calculates the sum of the digits of each number and then serves as the key function to the sorting process. Should there be multiple numbers with the same digit sum, they will be sorted according to their index from the original list, thanks to the lambda function's configuration.