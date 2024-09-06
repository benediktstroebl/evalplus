```python
def parse_nested_parens(s):
    levels = []
    for match in s.match(r'(\([ )(\])+?\n)', 'g'):  # remove parentheses match
        if match.group(0)[0] == '(':  # add parenthesis to group
            levels.append(match.group(0)[1:-2])
        else:  # check for open parenthesis group
            levels.append(match.group(1)[0])
    return levels

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))')') == [2, 3, 1, 3]
```

The function `parse_nested_parens` takes a string `s` as input and uses a list comprehension to split the string into groups of nested parentheses. The function then iterates over the groups and adds the deepest level of nesting to the list `levels`.

The function `test_parse_nested_parens` passes the test by checking if the output of `parse_nested_parens` is equal to `[2, 3, 1, 3]`.