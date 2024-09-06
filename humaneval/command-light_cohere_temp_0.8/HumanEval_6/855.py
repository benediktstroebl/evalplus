```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for match in s:
        if match == '(': stack.append(1)
        elif match == ')':
            if not stack or stack[-1] == 1:
                output.append(0)
                stack.append(0)
            else:
                stack.append(stack.pop())
   mate
    one: match is not ')', stack.append(1)
        else:
                stack.pop()
                stack.append(1)
   return: list(output)
    return output
#Tests
test_input = '(()()) ((())) () ((()))'
test_output = parse_nested_parens(test_input)
assert test_output == [2, 3, 1, 3]
```