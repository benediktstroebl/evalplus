```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list l are below threshold t, False otherwise.
    """
    return all(num < t for num in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected: False
```

This script defines a function `below_threshold` which takes a list of numbers and a threshold value as input. The function uses the built-in `all()` function along with a generator expression to check if all numbers in the list are below the threshold. The test cases at the end demonstrate how to use the function.