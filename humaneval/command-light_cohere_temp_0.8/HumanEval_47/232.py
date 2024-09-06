```python
def median(lst):
    """Return the median of list lst."""
    return (sum(lst)/2) if len(lst)%2 else lst[(len(lst)-1]  )

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3]) == 3.0
assert median([10, 20, 30, 40, 50]) == 30.0
assert median([10, 20, 30]) == 30.0
```
This function takes a list of numbers as an argument, and returns the median of the list. The function works by calculating the sum of the elements in the list, then dividing the sum by 2 to get the average. The function then returns the average as the median.