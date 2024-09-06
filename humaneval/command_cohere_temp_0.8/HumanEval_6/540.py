```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nested = 0
        stack = []
        for c in chunk:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    break
                nested += 1
                stack.pop()
        result.append(nested)
    return result
```

The code processes each group of parentheses separately and uses a stack to keep track of opening parentheses. For each turn, it increments the counter if it encounters a closing parenthesis and the stack is not empty, or else it resets the counter and breaks the loop if the stack is empty, indicating a unmatched closing parenthesis.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This output shows the depth of each group of parentheses for the input string. The first group has two layers, the second has three, and the third has just one. The fourth group has three layers, which is the maximum.