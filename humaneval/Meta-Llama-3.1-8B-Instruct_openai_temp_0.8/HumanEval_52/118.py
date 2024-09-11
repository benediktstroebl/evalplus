```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.

    Args:
    l (list): A list of integers.
    t (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < t for i in l)

# Example use cases:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of integers and a threshold value. It uses the built-in `all` function with a generator expression to check if all numbers in the list are less than the threshold. The function returns `True` if the condition is met and `False` otherwise.

The script also includes example use cases in the `if __name__ == "__main__":` block to demonstrate how to use the `below_threshold` function.