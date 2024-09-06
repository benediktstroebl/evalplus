```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        imbalance = 0
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
                imbalance += 1
            else:
                if not stack or stack[-1] != '(':
                    imbalance -= 1
                else:
                    imbalance += -1
                stack.pop()
            level = max(level, imbalance)
        result.append(level)
    return result
```

The approach employed by the function involves splitting the input string into segments based on spaces, and for each segment, it maintains a level which is the maximum depth of nesting of parentheses. The level is tracked using a stack where '(' char is pushed and ')' is popped. The imbalance counter is used to count the imbalance of '(' and ')' characters, and the maximum of imbalance and stack size gives the deepest level of nesting in that segment. Finally, the function returns a list of these levels for each segment. 

Here is an example usage of the function and its corresponding output:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```