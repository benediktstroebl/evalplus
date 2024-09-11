```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Should print True
print(monotonic([1, 20, 4, 10]))  # Should print False
print(monotonic([4, 1, 0, -10]))  # Should print True
```
This script defines a function `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It uses the `all` function to check if each pair of adjacent elements in the list satisfies the condition for increasing or decreasing order. The function returns `True` if the list is either increasing or decreasing, and `False` otherwise. The script also includes three test cases to demonstrate the function's behavior.