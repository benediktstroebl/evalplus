```python
def parse_nested_parens(s):
    """
    Function to parse nested parentheses.
    """
    expected input: string represented multiple groups for nested parentheses separated by spaces.
    """
    expected output: list of deepest level of nesting of parentheses """
    return [eval[0] for eval in (eval.get(0) for sub in s.} if sub == '(']')]

def test_parse_nested_parens():
    """
    Function to test the parse_nested_parens function
    """
    # Test with valid input
    test_str = "(()()) ((())) () ((()))"
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]

    # Test with invalid input
    test_str = "aa"
    with pytest.raises(Exception):
        parse_nested_parens(test_str)

# Run the function tests
test_parse_nested_parens()
```

The provided Python script defines a function `parse_nested_parens` that parses a string representing multiple groups of nested parentheses separated by spaces. It uses list comprehension and evaluates expressions inside parentheses to identify the deepest level of nesting. The function is then tested using a test function `test_parse_nested_parens`, which contains a series of valid and invalid test cases to verify the function's correctness.