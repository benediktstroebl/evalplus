```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold."""
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

In this script, we define a function `below_threshold` that takes a list `lst` and a threshold `threshold` as input. The function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, `all` returns `True`, otherwise it returns `False`.