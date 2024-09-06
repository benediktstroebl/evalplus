```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        stack = []
        num = 0
        for char in bracket_group:
            if char == '(':
                stack.append(char)
            else:
                num += 1
                while stack and stack.pop() != '(':
                    pass
                result.append(num)
    return result
```
The code uses a stack to track the nest level for each opening parenthesis and increments a counter when it encounters a closing parenthesis. The maximum counter value across all groups provides the deepest level of nesting for that particular group. The overall time complexity is O(N) where N is the size of the string.