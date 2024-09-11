```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.

    Example:
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

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input. It iterates over the list, adding each number to a set. If it encounters a number that is the negative of a number it has already seen, it immediately returns `True`, indicating that there are two distinct elements that sum to zero. If it finishes iterating over the list without finding such a pair, it returns `False`. The script includes test cases to demonstrate its correctness.