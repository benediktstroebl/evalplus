```python
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases for function:
test_filter_integers = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
    [10, 40, 30, 20],
    [None, 5, '6', 7]
]

assert filter_integers(test_filter_integers) == [10, 40, 30, 20, None, 5, 7]
```