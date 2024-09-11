```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The maximum allowed value.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, we define a function `below_threshold` that takes a list of numbers `lst` and a threshold `threshold` as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns True as long as all elements of the iterable (in this case, the generator expression) are True. The generator expression iterates over the numbers in the list and checks if each number is less than the threshold. If at least one number is not less than the threshold, the `all` function returns False immediately.