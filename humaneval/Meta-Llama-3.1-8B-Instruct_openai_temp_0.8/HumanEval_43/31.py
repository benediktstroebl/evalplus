```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Should return False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Should return False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Should return False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Should return True
print(pairs_sum_to_zero([1]))  # Should return False
```
This script uses a set to keep track of the numbers we've seen so far. If we encounter a number's negation (i.e., the number that would sum to zero with it), we immediately return `True`. If we get through the entire list without finding such a pair, we return `False`.