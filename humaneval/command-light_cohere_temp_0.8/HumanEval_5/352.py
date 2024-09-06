```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [1, 2, 3, 4, 10, 20]
test_delimiter = 4
test_expected = [1, 5, 7, 9, 14, 18]

def test_function(func: intersperse, test_data: List[int], test_delimiter: int) -> None:
    actual = func(test_data, test_delimiter)
    assert actual == test_expected, "Test failed"

test_function(intersperse, test_data, test_delimiter)
```

This code provides a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a list with numbers separated by that delimiter. The test case uses a numbers and a delimiter, then asserts that the function works correctly.