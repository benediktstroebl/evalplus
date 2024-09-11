```python
def below_threshold(lst: list, t: int) -> bool:
    """Return True if all numbers in the list lst are below threshold t.
    
    Args:
    lst (list): A list of numbers.
    t (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < t for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value, and returns True if all numbers in the list are below the threshold, and False otherwise. The function uses the built-in `all` function in combination with a generator expression to check this condition. The script then includes example usage of the function to demonstrate its behavior.