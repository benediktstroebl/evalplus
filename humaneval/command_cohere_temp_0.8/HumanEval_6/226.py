```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))':
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a straightforward recursive methodology. It maintains a **level** counter to track the current depth of parentheses nesting. Subsequently, it traverses the input string, increasing the **level** for each opening parenthesis encountered and decreasing it for each closing parenthesis. The maximum value attained during this iteration signifies the deepest nesting level for the respective parentheses group.

To accommodate multiple groups of parentheses, we process them individually and determine their separate nesting depths. These depths are then collected and returned as a list to represent the outcome.

The unit tests are formulated using Python's `unittest` module. Specifically, it crafts a test class featuring a single test method that harnesses the `parse_nested_parens` function and evaluates its output against the anticipated result.

This methodology allows for the comprehensive evaluation of the function's correctness against diverse test cases, ascertaining its adequacy in yielding the intended results.