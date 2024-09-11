```python
def below_threshold(lst: list, t: int) -> bool:
    """Return True if all numbers in the list lst are below threshold t."""
    return all(i < t for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected: False
```

In this script, we define a function `below_threshold` that takes a list `lst` and an integer threshold `t` as arguments. The function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are less than the threshold. If the condition is met for all numbers, the function returns `True`; otherwise, it returns `False`. 

The test cases at the end verify the function's behavior for the example scenarios provided in the problem.