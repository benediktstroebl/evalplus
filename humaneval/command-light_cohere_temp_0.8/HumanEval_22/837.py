```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', },
    [], None]

print("Test case 1:")
assert filter_integers(values_test) == [5]

print("Test case 2:")
assert filter_integers(values_test) == [1, 2, 3]

print("Test case 3:")
assert filter_integers([1, 2, 3, 'abc', }) == ['abc']

print("Test case 4:")
assert filter_integers(values_test) == []

print("Test case 5:")
try:
    assert filter_integers(None) is None
except AssertionError as e:
    print(f"Error: {e}" )
```