```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s.open():
       
        matchlevel = 1
        while match:
            if match.startswith('('('):
                stack.append(matchlevel)
                match = match[1:]
            elif match.startswith(') and matchlevel == 1:
                result.append(matchlevel)
                stack.append(match)
            matchlevel += 1
            else:
                stack.append(match)
        match = match[1:]
    return result
```