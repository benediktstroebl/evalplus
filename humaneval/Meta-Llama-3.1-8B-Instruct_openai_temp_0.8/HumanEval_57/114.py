```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

In this script, the `monotonic` function checks if a list of numbers is either monotonically increasing or decreasing. The function uses two helper generator expressions to check for both increasing and decreasing lists, and returns True if either condition is met. The test cases at the end of the script demonstrate how the function works with different inputs.