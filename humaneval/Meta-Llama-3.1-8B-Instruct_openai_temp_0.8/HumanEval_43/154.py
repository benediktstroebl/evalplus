```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether there are two distinct elements in the list that sum to zero.

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
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Expected output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Expected output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Expected output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Expected output: True
print(pairs_sum_to_zero([1]))  # Expected output: False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements that sum to zero, and `False` otherwise. It uses a set to keep track of the numbers it has seen so far, and checks if the negation of each number is in the set. If it finds a matching pair, it immediately returns `True`. If it finishes iterating over the list without finding a pair, it returns `False`. The script also includes test cases to verify that the function works correctly.