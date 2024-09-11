### Pairs Sum To Zero
#### Problem Description
Given a list of integers, determine if there are two distinct elements in the list that sum to zero.

#### Solution
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        bool: Whether two distinct elements sum to zero.
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
#### Explanation

This script works by iterating over the list of integers and keeping track of the numbers we have seen so far in a set called `seen`. For each number, we check if `-num` (its negative counterpart) is in the `seen` set. If it is, we return `True` because we have found two numbers that sum to zero. If we finish iterating over the list without finding a pair of numbers that sum to zero, we return `False`.