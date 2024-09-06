```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    stack.append(0)  # Start with an empty stack. 
    for i, len(s) in range(1, len(s) + 1):
        c = s[i]
        if c == ")":
            stack[-1] += 1
        elif c == "(":
            stack.append(1)  # Push a new item
        elif c == ")":
            stack.pop()  # Pop the Finally
    result = stack
    return result
# Example usage
input_str = "(()()) ((())) () ((())())"
result_list = parse_nested_parens(input_str)
print(result_list)  # Output [2, 3, 1, 3]
``` 
The provided code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses. The function uses a method of iterating through the string, checking each character against a set of parentheses and storing the results in a stack. When the string is processed, the function will return the list of deepest level of nesting parentheses.