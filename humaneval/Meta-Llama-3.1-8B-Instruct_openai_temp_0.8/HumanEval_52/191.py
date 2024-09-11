```python
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t."""
    
    # Use the built-in all() function in combination with a generator expression
    # to check if all numbers in the list are below the threshold
    return all(i < t for i in l)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `all()` function returns `True` if all elements in the iterable (in this case a generator expression) are true. The generator expression `(i < t for i in l)` checks each number `i` in the list `l` to see if it's less than the threshold `t`.