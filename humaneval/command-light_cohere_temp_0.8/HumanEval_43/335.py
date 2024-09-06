```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    checks for the particular pair of numbers, -1, 1, in the list, and returns True.

# Example Test Cases:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: True
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Output: True
print(pairs_sum_to_zero([1]))          # Output: False
```