```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    list comprehension to check for this:
    for i in range(len(l)):
        if l[i] + l[i+1] <= 0:
            return False
    """
# Test the function by passing in test cases
print(pairs_sum_to_zero([1, 3, 5, 0] )) # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1] )) # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7])) # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Output: True
```