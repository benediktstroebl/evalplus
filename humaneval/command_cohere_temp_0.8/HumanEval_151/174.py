Here's a Python script with a self-contained function that solves the problem and includes helpful comments and appropriate tests:
```python
import numpy as np

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    # Convert the list to an array for easier manipulation
    arr = np.array(lst, copy=True)
    
    # Check if the input list is empty, return 0 if it is
    if arr.size == 0:
        return 0
    
    # Convert integers to floats to avoid integer overflow during square operation
    arr = arr.astype(float)
    
    # Square the numbers and convert to numpy array
    odd_numbers = np.where(arr % 2 == 1, arr ** 2, 0)
    odd_numbers = np.array(odd_numbers)
    
    # Sum the squared odd numbers
    result = np.sum(odd_numbers)
    
    return result

# Example usage
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0  # This should also return 0

# Test with an empty list
empty_list = []
assert double_the_difference(empty_list) == 0
```

In this script, we leverage `numpy` for integer manipulation and boolean operations, resulting in a more concise solution. The function handles empty lists and odd squares summing seamlessly.

Note: While the `numpy` library is powerful for such numerical operations, it does add an extra dependency. If your project is focused solely on list manipulation, you may opt for a more straightforward Python solution. However, if you're working with numerical data often, `numpy` can be a valuable tool.