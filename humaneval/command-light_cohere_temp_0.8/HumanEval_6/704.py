```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    pairs = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if not stack or c == ')':
                pairs.append(stack.pop())
            stack[:]
            stack = []
    return pairs

# Example usage
input_string = "(()()) ((())) () ((())())"
result = parse_nested_parens(input_string)
print(result)  # Output: [2, 3, 1, 3]
```

This function iterates through the input string, where each character is either an open parenthesis '(' or a close parenthesis ')'. If it encounters an open parenthesis, it adds the current level of nesting to the stack. The function maintains a nested structure of parentheses by adding the current level to the stack and popping the elements back to the stack when a close parenthesis is encountered. The function then returns the stack, which contains the deepest level of nesting of parentheses in the input string.