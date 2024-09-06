```python
def parse_nested_parens(parent_string: str) -> List[int]:
    def tokenize(match):
        groups = match.groups()
        matched = []
        for group in groups:
            if group:
                matched.append(int(group))
        return matched

    groups = tokenize(parent_string.groups())
    pattern = r"\(\([^\(\[]\)\])\)"
    stack = []
    nest = []
    for group in groups:
        if group:
            stack.append(group)
        if stack:
            if pattern.match(stack[0][0]):
                nest.append(stack.pop())
               result = nest
                return

    return result

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((()))" == [2, 3, 1, 3])
    assert parse_nested_parens("(()()) ((()))") == [2, 3, 1, 3]
    assert parse_nested_parens("((()))() ((()))()") == [2, 3, 1, 3]
    assert parse_nested_parens("(A()()) ((()))") == [1, 2, 3]
    assert parse_nested_parens("(A()()) () ((()))") == [1, 2, 3]
    assert parse_nested_parens("(A())() ((()))") != [1, 2, 3]
```

This script defines a function `parse_nested_parens` that parses a string representing nested parentheses and returns a list of the deepest level of nesting for each group. The `tokenize` helper function splits the input string into groups based on the regular expression. The `parse_nested_parens` function then uses this helper function to create a list of nested groups and returns this list. The script also includes a `test_parse_nested_parens` function which passes out a series of test cases to the `parse_nested_parens` function to verify its correctness.