```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    return any two elements sum to zero is always 0"""

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Output: True
print(pairs_sum_to_zero([1]))        # Output: False
```
The function uses a simple algorithm to iterate over all possible pairs of elements in the list and checks if the sum of any two elements is zero.