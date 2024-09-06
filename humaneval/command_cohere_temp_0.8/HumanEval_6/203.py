```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        depth = 0
        for char in segment:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                depth = stack.pop()
        result.append(depth)
    return result
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integer values. This function is designed to solve the problem of parsing and evaluating the deepest level of nesting of parentheses in a given string composed of multiple groups of nested parentheses separated by spaces.

Here's how the function works:
1. The input string `s` is split into segments, where each segment represents a group of nested parentheses.
2. For each segment, the function uses a stack to keep track of the level of parentheses encountered.
3. When an open parenthesis `(` is encountered, it is added to the stack, and the depth is increased.
4. When a close parenthesis `)` is encountered, the depth is decreased by popping the top of the stack.
5. The final depth value for each segment represents the deepest level of nesting of parentheses in that segment.
6. The function assembles a list of these depth values, representing the outcome for each group of nested parentheses in the input string.

This solution is self-contained and provides a clear and concise way to solve the problem using basic Python concepts, making it an ideal solution for situations where cleanliness and efficiency are valued.