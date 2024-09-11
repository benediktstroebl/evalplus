**Pairs Sum to Zero**
======================

### Problem Statement

Given a list of integers, return `True` if there exist two distinct elements that sum to zero, and `False` otherwise.

### Solution

```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether two distinct elements in the list sum to zero.
    """
    seen = set()
    for num in lst:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False
```

### Example Use Cases

```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

### Explanation

The `pairs_sum_to_zero` function uses a set `seen` to keep track of the numbers we've seen so far. For each number `num` in the input list, we calculate its complement `complement = -num`. If `complement` is already in `seen`, we return `True` because we've found two distinct numbers that sum to zero. Otherwise, we add `num` to `seen` and continue to the next number. If we finish iterating over the list without finding a pair of numbers that sum to zero, we return `False`.