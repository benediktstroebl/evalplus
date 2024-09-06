```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nesting = 0
        unbalanced = 0
        stack = []
        for c in chunk:
            if c == '(':
                stack.append(c)
                nesting += 1
                unbalanced += 1
            elif c == ')':
                unbalanced -= 1
                if not unbalanced:
                    nesting += 1
                    result.append(nesting)
                    stack.pop()
                else:
                    stack.append(c)
            unbalanced += (c == '(')
        if stack:
            result.append(nesting)
    return result
```

The code processes each token of the string separately and uses a stack to keep track of nesting level for current token. The loop goes through characters of the token and increases/decreases nesting level depending on encountered parentheses. Once the loop is done with processing, the result is a list of deepest nesting levels for each token.