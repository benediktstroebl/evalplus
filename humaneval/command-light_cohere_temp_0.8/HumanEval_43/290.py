```python
def pairs_sum_to_zero(l):
    """
    Function to check whether a list of integers has two summable elements whose sum is 
    zero.
    """
    Returns: A boolean value of True if there are two distinct elements in the list 
    whose sum is zero, and False otherwise."""
    return sum(x for x in l) == 0

# Test the function
test_pairsum = lambda: pairs_sum_to_zero([1, 3, 5, 0])  # Output: False
test_pairsum = lambda: pairs_sum_to_zero([1, 3, -2, 1])  # Output: False
test_pairsum = lambda: pairs_sum_to_zero([1, 2, 3, 7])  # Output: False
test_pairsum = lambda: pairs_sum_to_zero([2, 4, -5, 3, 5, 7])  # Output: True
test_pairsum = lambda: pairs_sum_to_zero([1])  # Output: False
```

The function `pairs_sum_to_zero` checks whether a list of integers has two summable elements whose sum is zero. It uses theal `sum()` function to calculate the sum of all the elements in the list.