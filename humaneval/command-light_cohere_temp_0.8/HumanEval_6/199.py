```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s.group() or pattern("([ )]+", re.sub(r'([ )+", ")", str.match)) :
        match = match.group('([ )+', r')
        stack.append(1)
        while match = match
        for match in stack :
                i = len(match)
                if i > 3 :
                    result.append(i)
                    stack.append("")
                return result
    while stack != []
    return result
``` 
Output should be: [2, 3, 1, 3]