```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(1)
        elif char == ")":
            stack.pop()
            else:
                stack.push()
                i + 1
   
            result.append(stack.pop()
        stack[-1])
    return result
```

This function takes a string as input and iterates through each character in the string. It keeps track of the characters by using a stack, which it pushes new characters onto and pops from when a closing parent is encountered. The function then returns a result, which is a list of the deepest levels of nesting for each group of parentheses in the string.

Please note that you can use this function to solve the problem with any given input string.