```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [1]
        stack = [0]
        for char in segment:
            if char == '(':
                stack.append(open_brackets[-1]+1)
                open_brackets.append(open_brackets[-1]+1)
            elif char == ')':
                open_brackets.pop()
                stack.pop()
        result.append(max(stack))
    return result
```

The approach employs a stack to keep track of the opening brackets and a list to count the opening brackets. The maximum value in the stack reflects the deepest level of nesting of parentheses. 

The unit test based on the provided example input is updated as well. Here is the updated test:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())'
                                ) == [2, 3, 1, 3]
```