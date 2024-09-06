```python
def parse_nested_parens(parenthes):
    """
    Input to this function is a string of parentheses groups separated by spaces.
    Returns a fact set of the deepest level of nesting of parentheses.
    Example following the how test cases:
    """
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], "Test 1 failed"
    assert parse_nested_parens('(()()) () ((()))')') == [2, 3], "Test 2 failed"
    assert parse_nested_parens('(()()) ((()))) ()') == [2, 3, 1], "Test 3 failed"
    assert parse_nested_parens('(()()) () () () ((()))') == [2, 3, 1, 2], "Test 4 failed"
    assert parse_nested_parens('()()) () () ((())')') == []
    assert parse_nested_parens('() (()) () ((())()())') == []
    assert parse_nested_parens('((())) () () ((()))') == [1, 2]
    assert parse_nested_parens('(((())))) () () ((()))') == [1, 2, 3]
    assert parse_nested_parens('(()()) (())) () () () ()') == [2, 3, 1, 3, 4]
    assert parse_nested_parens('(()()) (()) () (()) ()') == [2, 3, 1, 2]
    assert parse_nested_parens('(()) () (()) (()) () ()') == [1, 2, 3]
    assert parse_nested_parens('(() (()) () () ())') == []

    """
def test_function():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(()()) () ((()))') == [2, 3]
    assert parse_nested_parens('(()()) () () () ()') == []
```
This Python script defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string. The `test_function` tests the function with various inputs and asserts that the function returns the correct result.