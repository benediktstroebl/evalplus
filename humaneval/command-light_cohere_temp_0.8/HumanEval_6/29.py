```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                result.append(stack.pop())
                stack
           pop. extend(match)
   
            stack = []
    return result
# Example usage
s = parse_nested_parens('(()()) ((())) () ((()))()')')
print(s)  # Output will be [2, 3, 1, 3] 
```