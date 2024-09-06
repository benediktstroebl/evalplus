```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Testing the function
test_values = [1, 2, 3, 'abc', float('3.14'), 5]
assert filter_integers(test_values) == [1, 2, 3, float('3.14'), 5],
print("Test passed!")
```