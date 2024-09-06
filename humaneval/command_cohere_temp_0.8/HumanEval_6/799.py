```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')).split('(') for _ in range(2)]):
        stack = [0]
        while opening != closing:
            while stack and not stack[-1]:
                stack.pop()
            stack.append(opening != ')')
            opening = opening.replace(')', '')
            closing = closing.replace('(', '')
        result.append(len(stack))
    return result
```

The approach for this problem is to iterate through each bracket group in the string and perform the following steps:
1. Push an initial zero onto a stack to represent the depth of the root node.
2. Iterate through each character in the bracket group:
  - If the character is an opening bracket, do the following:
   - Increment the top of the stack (depth of the tree).
   - If the stack is empty or comprises only closing brackets, push an opening bracket marker (i.e., True) onto the stack to track the presence of an opening bracket.
3. Once the opening and closing brackets for a particular group have been iterated through, the stack will contain the necessary information to calculate the depth of the group. Simply count the number of elements in the stack to obtain the depth.

This approach allows us to efficiently calculate the depth of each bracket group in the provided string.