```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input, which is supposed to contain multiple groups of nested parentheses separated by spaces. This function calculates and returns the deepest level of nesting of parentheses for each group.

The core logic iterates through the characters of each input group and maintains a stack of depths, where each depth value represents the current nesting level. When an opening parenthesis `(` is encountered, the stack is pushed with the current depth plus one. When a closing parenthesis `)` is encountered, the stack is popped to retrieve the previous depth.

The provided example in the Markdown code snippet demonstrates the behavior of this function on a sample string and shows how it returns a list of deepest nesting levels for each group of parentheses.

This solution is type-hinted using the `typing` module to ensure the function accepts the expected input type and returns the appropriate output list of integer depths.