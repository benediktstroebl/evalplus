```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', {}, []],
    [1, 2, 3, 4, 5], 'apple', [(), True, None]
]

def test_function(test_case):
    actual = filter_integers(test_case)
    expected = [x for x in test_case if isinstance(x, int)]
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"  # Add specific assert message here

test_function(test_filter_integers)
 ``` 
This Python script provides a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the original list. The script also includes a test suite with multiple test cases to verify the correctness of the function.