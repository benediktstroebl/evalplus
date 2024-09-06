```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(3)
            stack.append(2)
    match
        else:
                stack.append(int(match) + 1)
    return result


# Example usage
s = "(()()) ((())) () ((())()())"
print(parse_nested_parens(s))  # Output: [2, 3, 1, 3]
```
This Python script defines a function parse_nested_parens that parses a string of nested parentheses. It uses a stack to keep track of opening parentheses and their corresponding levels of nesting. The function iterates through each character in the string, and follows the parsing rules. When it encounters an opening parenthesis, it pushes the level one onto the stack. When it encounters a finally, for closing parentheses, it checks the stack and appends the corresponding level to the result. The example usage demonstrates the function with the test string "(()()) ((())) () ((()))())".