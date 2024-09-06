```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                result.append(i)
            stack.append(char)
   else:
                stack.pop()
    important spaces because spaces, since the current character is not '(', we need to remove the last character on the stack before appending the current character.