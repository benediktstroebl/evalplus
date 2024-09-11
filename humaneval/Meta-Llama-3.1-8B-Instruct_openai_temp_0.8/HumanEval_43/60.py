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
    # Create a set to store the elements we have seen so far
    seen = set()
    for num in lst:
        # For each number in the list, check if its negation is in the set
        if -num in seen:
            # If we find a pair that sums to zero, return True
            return True
        # If not, add the number to the set
        seen.add(num)
    # If we have iterated over the entire list and found no pairs that sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

In this code, we use a set `seen` to keep track of the elements we have seen so far. For each number in the list, we check if its negation is in the set. If it is, we return True because we have found a pair that sums to zero. If not, we add the number to the set and continue iterating. If we have iterated over the entire list and found no pairs that sum to zero, we return False.