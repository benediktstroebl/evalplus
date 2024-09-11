```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.

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
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test the function
print(pairs_sum_to_zero([1, 3, 5, 0])) # False
print(pairs_sum_to_zero([1, 3, -2, 1])) # False
print(pairs_sum_to_zero([1, 2, 3, 7])) # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
print(pairs_sum_to_zero([1])) # False
```

This script uses a set to keep track of the numbers we've seen so far. It iterates through the list and checks if the negation of the current number is in the set. If it is, it immediately returns True. If it iterates through the entire list without finding a pair that sums to zero, it returns False.