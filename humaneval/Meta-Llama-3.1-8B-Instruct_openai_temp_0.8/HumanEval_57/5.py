```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(l) == 0:
        return True
    
    # Check if the list has only one element
    if len(l) == 1:
        return True
    
    # Check if the list is monotonically increasing or decreasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # True
print(monotonic([1, 2, 3, 2, 1]))  # False
print(monotonic([]))  # True
print(monotonic([1]))  # True
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the elements are monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check if the list is increasing or decreasing, and returns `True` if either condition is met. The script also includes test cases to verify the functionality of the `monotonic` function.