```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    opening_level = 0
    for char in parenthes_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if stack:
                result.append(stack.pop())
            maximum_ stack)
            opening_level -= 1
            stack = []
        elif opening_level > 0:
            stack.append(opening_level)
        opening_level = 0
    return result

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') is [2, 3, 1, 3]
```

The above code defines a `parse_nested_parens` function that parses and returns the deepest level of nesting of parentheses in a given string. The `test_parse_nested_parens` function verifies that the `parse_nested_parens` function returns the correct result for a given string. 

This problem is solved using a stack to keep track of opening parentheses and a counter to keep track of the deepest level of nesting.