Here is a self-contained Python function that solves the problem you have described:

```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Unit tests
def test_filter_integers():
    values_test = [1, 2, 3, 'abc', 0, 5, float('inf')]
    expected_test = [1, 2, 3, 0, 5]
    actual = filter_integers(values_test)
    assert actual == expected_test

if __name__ == "__main__":
    test_filter_integers()
```

This code provides a function **`filter_integers`** that accepts a list of values and returns a new list containing only the integers from the input. The test function **`test_filter_integers`** is also provided, which includes a set of values and expected integers, then it verifies that the output of the **`filter_integers`** function matches the expected output. 
Finally, the **`if __name__ == "__main__":`** block allows the script to be executed when the script is run directly, which is useful for testing the script and verifying its correctness.