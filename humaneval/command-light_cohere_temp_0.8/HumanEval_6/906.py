Here is a self-contained Python script that solves the problem of finding the deepest level of nesting of parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    in_list = False
    for i, char in enumerate(s):
        if char == "(":
            if not in_list:
                stack.append(1)
            in_list = True
        elif char == ")":
            if in_list:
                stack.append(len(stack))
                in_list = False
            else:
                stack.append(0)
        elif char == " ":
                if not in_list:
                    stack.append(1)
                    in_list = True
    return stack
#Example usage
test_string = "((()()) ((())) () ((()))())"
result = parse_nested_parens(test_string)
print(result)
```

This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack to keep track of the levels of opening parentheses, ensuring that each closing parent is paired with its corresponding opening parent at the same level. 

The function iterates through the string, keeping track of in-list states for parenthesis and list elements. The output is the stack, which will contain the levels of nesting of parentheses in the string.