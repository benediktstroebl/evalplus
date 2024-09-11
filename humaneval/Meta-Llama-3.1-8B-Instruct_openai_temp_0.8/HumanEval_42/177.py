```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [i + 1 for i in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation:

*   The function `incr_list` takes a list `l` as input and returns a new list where each element is incremented by 1.
*   It uses a list comprehension to achieve this. List comprehensions are a compact way to create lists from existing iterables.
*   The expression `i + 1` is evaluated for each element `i` in the input list, and the results are collected into a new list.
*   The `-> list` annotation indicates that the function returns a list. This is a type hint that can help other developers understand the function's behavior and can also be used by static type checkers.
*   The test code at the end demonstrates the function's usage with the provided example lists.