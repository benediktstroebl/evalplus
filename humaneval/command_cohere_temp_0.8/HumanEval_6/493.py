```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [1]
        stack = [0]
        for char in segment:
            if char == '(':
                open_brackets.append(open_brackets[-1] + 1)
            else:
                open_brackets.pop()
                stack.append(open_brackets[-1])
        result.append(stack[-1])
    return result
```

The code processes each segment of the input string independently. It maintains a stack of the number of open brackets encountered so far while iterating through each character of a segment. The maximum value amongst the stack corresponds to the deepest level of nesting for the given segment. The final answer is a list of these values for each segment, which is the output of the function.