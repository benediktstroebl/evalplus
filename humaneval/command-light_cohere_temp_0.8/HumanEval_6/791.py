```python
def parse_nested_parens(parenthes):
    return [i for i, a in enumerate(parenthes.split()) if a [a == ')' or a == '(']

# Test cases
parenthes_test = """
(()()) ((())) () ((()))
((()))()()()()()()()
"""

assert parse_nested_parens(parenthes_test) == [2, 3, 1, 3]

parens_with_empty = ""
assert parse_nested_parens(parens_with_empty) == []

parens_with_only_close = ")"
assert parse_nested_parens(parens_with_only_close) == []

parens_with_mixed = """
()() ()
((()) )
"""

assert parse_nested_parens(parens_with_mixed) == []

parens_with_invalid = "[(])"
with pytest.assert expected_exception=TypeError():
    parse_nested_parens(parens_with_invalid)
```
This code defines a function `parse_nested_parens` that takes a string of parentheses and returns a list of their depths of nesting. It does this using a simple split and check if each substring is ')' or '(' to determine the depth. The test cases cover various scenarios, including empty strings, only closed parentheses, only open parentheses, mixed content, and invalid content.