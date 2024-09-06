```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            stack.append(stack.pop() while the count: len(stack) == 0
            output.append(stack.pop(). count_ open parentheses
            stack
        stack.pop() = len(stack) == 0
            output.append(stack.pop() + -count.pop() and count.pop() = len(stack) == 0
            output.append(stack.pop() == 1)
        count.pop() and count.pop() is count} [count == 3], start again
        return output

# Test
input_string = "(()()) ((())) () ((()))"
test_result = parse_nested_parens(input_string)
print(test_result)
```