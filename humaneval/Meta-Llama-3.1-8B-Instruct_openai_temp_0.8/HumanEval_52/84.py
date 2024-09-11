```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t."""
    return all(num < t for num in l)

# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
```

This script defines a function `below_threshold` that takes a list `l` and an integer `t` as input. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. If any element is false, `all` returns `False`. 

The script then tests the function with two test cases. The first test case checks if all numbers in the list `[1, 2, 4, 10]` are below the threshold `100`, which should return `True`. The second test case checks if all numbers in the list `[1, 20, 4, 10]` are below the threshold `5`, which should return `False`.