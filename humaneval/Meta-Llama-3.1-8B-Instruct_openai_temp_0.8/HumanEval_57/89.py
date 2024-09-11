```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if not l:
        return True
    
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([]))  # True
```

This script defines a function `monotonic` that takes a list of integers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses Python's built-in `all` function to check if all elements in the list satisfy a given condition, and also checks if the list is empty. The test cases at the end of the script verify the correctness of the function.