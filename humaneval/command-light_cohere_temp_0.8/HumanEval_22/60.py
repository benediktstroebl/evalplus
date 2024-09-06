Here is a self-contained Python script that solves the problem of filtering out non-integer values from a list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    ['a', 3.14, 5],  # Contains float and integer
    [1, 2, 3, 'abc', {}, []],  # Contains object, string, and integers
    ]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert isinstance(actual, list), "test case failed: {}"
    assert all(isinstance(item, int) for item in actual), "test case failed: {}"
```
The script defines a function **filter_integers** that filters a list of values and returns a new list containing only the integer values. 

The script also includes several test cases that pass the filtering process and assert the resulting lists are of type **int**.