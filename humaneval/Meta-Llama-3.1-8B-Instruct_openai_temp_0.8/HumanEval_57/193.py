```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    
    # Check if the list is empty or contains one element
    if len(lst) < 2:
        return True
    
    # Check if the list is monotonically increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([]))  # True (empty list is considered monotonic)
print(monotonic([1]))  # True (list with one element is considered monotonic)
```

This script defines a function `monotonic` that checks if a given list is monotonically increasing or decreasing. The function uses the `all` function with a generator expression to check if all adjacent elements in the list are in the same order (either increasing or decreasing). The example usage demonstrates the function's behavior with various inputs.