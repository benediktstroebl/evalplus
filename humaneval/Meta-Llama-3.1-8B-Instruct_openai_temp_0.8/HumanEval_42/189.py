Here's a self-contained Python script that solves the problem:

```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this script, we use a list comprehension to create a new list where each element is equal to the corresponding element in the input list incremented by 1. The `-> list` annotation indicates that the `incr_list` function returns a list. The example usage demonstrates how to call the `incr_list` function with different inputs and print the results.