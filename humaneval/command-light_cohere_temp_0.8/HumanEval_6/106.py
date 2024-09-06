```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s.match(r'(()(.).o))'):
        stack.append(1) if match.push(match[0])
    while stack: match = stack.pop()
        stack.append(0)
        if match: result.push(match[0])
    return result

# Example usage:
def test_parse_nested_parens(*args):
    assert parse_nested_parens('(()()) ((())) () ((()))()') == [2, 3, 1, 3]
```