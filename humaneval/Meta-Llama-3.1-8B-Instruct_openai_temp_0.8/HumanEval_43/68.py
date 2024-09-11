Here's a Python script that solves the problem:
```markdown
## pairs_sum_to_zero.py

### Problem Description
Given a list of integers, determine if there exist two distinct elements that sum to zero.

### Solution
```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether two distinct elements sum to zero.
    """
    seen = set()  # Stores elements we've seen so far
    for num in lst:
        complement = -num  # The number that would sum to zero with num
        if complement in seen:  # We've seen its complement before
            return True
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the entire list without finding a pair
```

### Example Usage
```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set `seen` to keep track of elements we've seen so far. For each number in the list, we check if its complement (i.e., the number that would sum to zero with it) is in `seen`. If it is, we return True immediately, indicating that we've found a pair. If we iterate over the entire list without finding a pair, we return False.