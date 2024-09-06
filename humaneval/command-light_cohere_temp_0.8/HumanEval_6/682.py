```python
def parse_nested_parens(s):
    return [i for i, in parse(s, 0, s[i] == '(')]


def parse(s, start, fill):
    if start == len(s): return []
    for i, c in enumerate(s[start:], start + 1):
        if c == ')':
            if fill:
                return parse(s, i + 1, False)
            else:
                return [i]
        elif c == '(':
            fill = True
        else:
            fill = False
    return []
```
This code defines a function parse_nested_parens that takes a string s representing multiple groups of nested parentheses separated by spaces as input. The function then returns a list of indices corresponding to the deepest level of nesting for each group of open parentheses. The parse function uses a helper function parse to traverse the string and returns the list of indices of the deepest level of nesting for each group of open parentheses.