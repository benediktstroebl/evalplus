```python
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing."""
    
    # Compare the elements of the list with their neighbors to check for monotonicity
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
This script checks for both increasing and decreasing order in the list by comparing each element with its neighbor. If all pairs of neighbors are in order, it returns `True`, otherwise `False`.