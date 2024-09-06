Here's the self-contained Python function that solves the problem of finding the deepest level of nesting of parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of parentheses as input and returns a list of the deepest levels of nesting.
    :param s: The string of parentheses to be evaluated
    :return: A list of the deepest level of nesting, starting from 1 and incremented by 1 for each opening parenthesis
    """
    stack: List[int] = []
    stack.append(1)  # Create a list of the deepest level of nesting for each opening parenthesis
    for i, char in enumerate(s):
        if char == "(":
            stack.append(stack.pop() +1)
        deepest level = stack.append(1)
            stack.append(1)
        else:
            stack.pop()
            if stack:
                deepest_level = stack.pop()
                if deepest_level == 0:
                    stack.append(1)
                    stack.append(1)
        else:
                    stack.pop()
                    if stack:
                        deepest_level = stack.pop()
                    if deepest_level == 0:
                        stack.append(1)
                        stack.append(1)
                stack.append(1)
        else:
                        stack.pop()
                stack.append(1)
        return deepest_level
```

This function uses a stack to keep track of the deepest level of nesting for each opening parenthesis. It iterates through string character by character and checks if the character is an opening parenthesis. If it is, the current level is pushed onto the stack. If the character is a closing parenthesis, the stack is popped and the process continues until an opening parenthesis is encountered. The deepest level of nesting is returned as the last element in the stack.