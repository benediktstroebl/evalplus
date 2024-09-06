```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values_test = [1, 2, 3, 'abc', {}, [1, 2, 3])
result = filter_integers(values_test)
assert all(isinstance(x, int) for x in result), "The function didn't return integers."
```

The code defines a function **`filter_integers`** that accepts a list of values and returns a new list containing only the integers from the original input. It achieves this result by employing the `isinstance(x, int)` condition, which returns true if the item is an integer. The function is then tested using a sample **`values_test`** and the **`assert`** statement is used to check the results of the function against the expected output.