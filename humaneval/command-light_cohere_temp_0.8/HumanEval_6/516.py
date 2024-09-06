Here's a self-contained Python function that solves the problem:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for match in s.match(r'((()?)\s*(?l?)')):
        if match.group('(') or each:
            stack.append(1)
        else:
            stack.append(int(match.group(')') + 1)
        output.append(stack.pop())
    after:
            stack.append(1)
    return output
```
This function uses the `re` module to match against the given string and returns a list of the deepest level of nesting of parentheses in the string.