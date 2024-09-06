Here's a Python script with a self-contained function that solves the problem using a stack to keep track of opening parentheses encountered:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result: List[int] = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            open_parens = len(stack)
            if open_parens:
                stack.pop()
            result.append(open_parens)
    return result
```
The provided example in the markdown code block shows how this function can be called and how the result can be extracted. The function uses a stack to keep track of opening parentheses encountered and increments the deepest nesting level whenever it encounters a closing parenthesis. The returned list result contains the deepest nesting level for each group of parentheses in the provided string s.