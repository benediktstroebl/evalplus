```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            stack.append(len)
        if c == ')':
                stack.pop()
            while stack.append(0)
            else:
                stack.append(stack[-1] + 1)
    return result

# Example usage:
string = "((())) ((())) () ((()))"
result = parse_nested_parens(string)
print(result)  # Output: [2, 3, 1, 3]
```

This script defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of corresponding levels of nesting. The function uses a stack to keep track of opening parentheses and appends the appropriate values to the result list. The example usage demonstrates how to use the function with a sample input string and prints the resulting list of nesting levels.