```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for match in parentheses_string.match(r'\(\)(.*?)\)'):
        stack.append(match.pop()
    right to the match.
        content = match.group()
        anyway.content
       with rest in parentheses:
            if content.isalpha() andnot a parenthesis:
                result.append(1)
                else:
                    result.append(len)
    while stack:
                    level = stack.level
                    result.append(level)
                    result.append(level+done)
            stack = []
    return result
```