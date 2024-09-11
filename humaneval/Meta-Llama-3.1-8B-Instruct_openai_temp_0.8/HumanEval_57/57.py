```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is empty
    if len(l) < 2:
        return True
    
    # Check if list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if list is either monotonic increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([]))  # True
print(monotonic([1]))  # True
```
This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. It uses the `all` function to check if all adjacent elements in the list satisfy the condition of either being non-decreasing or non-increasing. The test cases are included at the end of the script to verify that the function works correctly.