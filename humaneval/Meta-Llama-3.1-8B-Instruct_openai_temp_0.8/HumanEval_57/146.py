```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): The input list.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehension to check if the list is increasing or decreasing. It then returns `True` if either condition is met, and `False` otherwise. The script includes test cases to verify the function's correctness.