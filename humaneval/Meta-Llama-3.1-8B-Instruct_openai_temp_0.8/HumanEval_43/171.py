```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Examples:
        >>> pairs_sum_to_zero([1, 3, 5, 0])
        False
        >>> pairs_sum_to_zero([1, 3, -2, 1])
        False
        >>> pairs_sum_to_zero([1, 2, 3, 7])
        False
        >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
        True
        >>> pairs_sum_to_zero([1])
        False
    """
    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in the input list that sum to zero. It uses a set `seen` to keep track of the numbers it has seen so far. If it encounters a number that is the negative of a number it has seen before, it immediately returns `True`. If it has checked all numbers without finding a pair that sums to zero, it returns `False`.