```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    
    # Check if the list is monotonically increasing
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 3, 2]))  # False
print(monotonic([5, 5, 5, 5]))  # True
```
This script defines a function `monotonic` that takes a list as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check if the list is increasing or decreasing, and returns `True` if either condition is met. The test cases at the end demonstrate the function's behavior with various inputs.