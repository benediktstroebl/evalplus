```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [1]
        stack = [0]
        for char in segment:
            if char == '(':
                open_brackets.append(open_brackets[-1] + 1)
            else:
                open_brackets.pop()
                stack.append(open_brackets[-1])
        result.append(stack[-1])
    return result
```
The code processes each segment of the input string separately, simulating nested brackets with a stack. The maximum depth of nesting for each segment is calculated and added to the result list. The overall time complexity is O(N), where N is the length of the input string.