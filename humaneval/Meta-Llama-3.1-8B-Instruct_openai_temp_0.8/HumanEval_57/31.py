```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(l) == 0:
        return True
    
    # Check if the first two elements are equal
    if l[0] == l[1]:
        # If they are equal, check if the list is monotonically increasing
        if all(l[i] <= l[i+1] for i in range(len(l)-1)):
            return True
        # If it's not monotonically increasing, check if it's monotonically decreasing
        elif all(l[i] >= l[i+1] for i in range(len(l)-1)):
            return True
        # If it's neither monotonically increasing nor decreasing, return False
        else:
            return False
    
    # If the first two elements are not equal, check if the list is monotonically increasing
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return True
    # If the list is not monotonically increasing, check if it's monotonically decreasing
    elif all(l[i] >= l[i+1] for i in range(len(l)-1)):
        return True
    # If it's neither monotonically increasing nor decreasing, return False
    else:
        return False


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 3, 7, 9]))  # False
print(monotonic([]))  # True
print(monotonic([1]))  # True
print(monotonic([1, 1]))  # True
```