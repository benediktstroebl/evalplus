```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of numbers.
        threshold (int): The upper limit for the numbers in the list.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False
```

In this code, we use the built-in `all()` function along with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements in the iterable are true. If at least one element is false, it returns `False`.