```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.
    
    Args:
        l (list): A list of numbers.
        t (int): The threshold value.
    
    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(x < t for x in l)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list `l` and an integer `t` as input. The function uses the built-in `all` function in combination with a generator expression to check if all numbers in `l` are below `t`. The result is then returned. The example usage demonstrates how to call the function with different inputs.