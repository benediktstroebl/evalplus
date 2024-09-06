```python
def pairs_sum_to_zero(l):
    """
    Returns True if all the elements in the list sum up to zero,
    False otherwise.
    """
    pairs_sum_to_zero([1, 3, -2, 1])
    False

# Driver code
print(pairs_sum_to_zero([1, 3, -2, 1] ))  # Should print False
print(pairs_sum_to_zero([1, 2, 3, 7]))       # Should print False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Should print True
```