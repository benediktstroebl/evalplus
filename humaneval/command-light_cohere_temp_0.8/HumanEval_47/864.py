```python
def median(lst):
    """Return median of elements in the list lst."""
    return float((len(lst) + 1) / 2) * (lst[(len(lst) / 2) - 1] + lst[len % 2])

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4]) == 3.0
assert median([10, 20, 30, 40]) == 10.0
``` 
This Python code defines a function `median` that computes the median of a list's elements. The median is calculated as the average of the two middle numbers and the middle number, with the average being the median. The code then tests the numbers and the function to ensure it is working correctly.