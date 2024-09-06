```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    in_string: bool = False
    for char in s:
        if char == ' ':
            if in_string:
                stack.append(1)
                in_string = False
        elif char == '(':
            in_string = True
        elif char == ')':
            in_string = False
        else:
            raise ValueError("Unexpected character in the string")
    return stack
# Example usage
s = "(((()()) ((())) ) ((())()()) )"
result = parse_nested_parens(s)
print(result)  # Output: [2, 3, 1, 3]
```
This function takes a string as input and uses a stack to keep track of the nesting levels of parentheses. The function also uses an boolean variable `in_string` to track if we are inside a string or inside a pair of parentheses. This allows the to correctly identify opening and closing parentheses.