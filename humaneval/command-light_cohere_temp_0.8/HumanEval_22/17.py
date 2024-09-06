```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases for function
values_test = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', }, {}]

print(filter_integers(values_test))
```