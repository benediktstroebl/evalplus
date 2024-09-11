```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether there are two distinct elements that sum to zero.

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
    if len(lst) < 2:
        # List must have at least two elements to have two distinct pairs.
        return False

    complements = set()
    for num in lst:
        # Check if the complement of num exists in the list.
        if num * -1 in complements:
            # If num's complement exists, return True.
            return True
        complements.add(num)

    # If no complements found, return False.
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

In this code, we first check if the list has less than two elements, in which case there cannot be two distinct pairs that sum to zero. Then, we iterate over the list and check if the complement of each number (i.e., its negation) exists in the list. If it does, we return True, because we have found two distinct numbers that sum to zero. If we finish iterating over the list without finding any complements, we return False, because we know that there are no distinct pairs that sum to zero.