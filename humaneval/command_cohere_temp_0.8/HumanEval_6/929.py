```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        depth = 0
        for c in token:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] != '(':
                    result.append(depth)
                while stack and stack.pop() != '(':
                    pass
                depth += 1
        if not stack:
            result.append(depth)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string as input. This string contains multiple groups of nested parentheses separated by spaces, and the function is designed to extract and compute the deepest level of nesting for each group.

Here's how it works:
1. **Data Structure**: The function utilizes a stack to keep track of open parentheses as it iterates through each token in the input string.
2. **Iterating Through Tokens**: The input string is split into individual tokens using the `split()` method, ensuring each group of parentheses is processed independently.
3. **Depth Calculation**: For each token, the function tracks the number of open parentheses (`(`) versus closed parentheses (`)`). When an open parentheses is encountered, it is added to the stack. When a closed parenthesis is encountered, the function checks if the last element in the stack is an open parenthesis. If it is not, that indicates the closing of a group, and the depth is incremented by 1. If it is, the function pops elements from the stack until an open parenthesis (denoting the end of the current group) is reached.
4. **Recording Depth**: The depth is incremented for each new group of parentheses and remains unchanged if a group is closed. The final depth of each group is recorded in the `result` list.

The provided example input string demonstrates how the function operates and produces the expected output.