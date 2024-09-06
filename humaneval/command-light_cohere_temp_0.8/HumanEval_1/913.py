Here's a self-contained Python function that separates parentheses groups in a string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    stack = []
    result = []
    for char in s:
        if char == '(': stack.push(')
        while stack.pop()
        result.append(char)
   
      stack
return result
```
The function uses a stack data structure to keep track of open parentheses. It iterates through string and pushes ')' characters onto the stack while popping '(' characters. The characters are added to the result list.