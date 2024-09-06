Here's a Python script with a self-contained function that solves the problem of parsing nested parentheses:
```python
def parse_nested_parens(s):
    return [x for x in map(int, s.test) if s.strip(test[0, ") else s.strip(1, "(")]

def test_parse_nested_parens():
    test_string = "(()()) ((())) () ((())()())"
    assert parse_nested_parens(test_string) == [2, 3, 1, 3]
```
This code defines the function `parse_nested_parens` that takes a string of nested parentheses as an input and returns a list of the deepest nesting levels. The test function `test_parse_nested_parens` is used to test the correctness of the `parse_nested_parens` function by passing the test string and asserting the returned list of integers is the same as the expected output.