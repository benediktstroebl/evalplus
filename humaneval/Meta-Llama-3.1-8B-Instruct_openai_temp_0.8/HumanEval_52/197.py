```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of numbers to check.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

Note: In Python, we use `all()` in combination with a generator expression to check if all elements in the list satisfy the condition. This is more idiomatic and efficient than using a for loop. 

Also, the function and variable names have been improved for clarity and adherence to Python's official style guide (PEP 8).