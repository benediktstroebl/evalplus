```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()
    for num in l:
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

This script contains the function `pairs_sum_to_zero` which checks for pairs of distinct elements in a list that sum to zero. It iterates over the list, keeping track of the elements seen so far in a set. If it encounters the negation of an element it has seen before, it returns `True`. If it has iterated over the entire list without finding such a pair, it returns `False`.