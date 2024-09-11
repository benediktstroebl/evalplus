### pairs_sum_to_zero Function

The following Python script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that sum to zero.

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    # Create a set to store unique elements
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If no two numbers sum to zero, return False
    return False

# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that iterates over the input list and keeps track of the numbers it has seen so far in a set. If it encounters a number that is the negative of a number it has seen before, it immediately returns `True`, indicating that there are two distinct elements in the list that sum to zero. If it finishes iterating over the list without finding such a pair, it returns `False`.