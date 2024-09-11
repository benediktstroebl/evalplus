```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks whether the elements of a list are monotonically increasing or decreasing. It uses the `all` function in combination with a generator expression to check whether all adjacent elements in the list satisfy the condition of being either less than or equal to (for increasing lists) or greater than or equal to (for decreasing lists) each other. The `or` operator is used to check for both increasing and decreasing lists. The test cases at the end of the script demonstrate the function's behavior.