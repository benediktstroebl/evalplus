```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The maximum allowed value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    # Use the built-in all() function with a generator expression to check if all numbers in the list are below the threshold
    return all(num < threshold for num in lst)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the `all()` function with a generator expression to perform the check efficiently. The script also includes a docstring to provide documentation for the function, and includes some test cases to demonstrate its usage.