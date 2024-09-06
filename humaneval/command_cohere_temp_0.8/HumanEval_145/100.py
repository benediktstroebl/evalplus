```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```

The function `order_by_points` sorts the list of numbers `nums` by the sum of the digits of each number. For ties, it uses the index of the number in the original list as a secondary sort key. Test cases are provided to verify the function. The `sorted` function is used with a custom key function to sort the list accordingly. The code is self-contained and can be executed directly to test and verify the function.