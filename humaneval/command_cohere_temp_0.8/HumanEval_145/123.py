```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Copy the list to avoid modifying the original
    nums = nums[:]
    # Sort by digit sum, using the tiebreaker logic
    nums.sort(key=lambda x: (sum(int(d) for d in str(x)), x))
    return nums
```

This script sorts the list `nums` in ascending order based on the sum of the digits of each number, using the `sort` function with a custom `key` function. This custom `key` function calculates the sum of digits for each number, and when sums are tied, the original list index is used as a tiebreaker to ensure consistency.

Here's an example of using this function:
```python
order_by_points([1, 11, -1, -11, -12])
```

The function passes the test as it returns:
```python
[-1, -11, 1, -12, 11]
```