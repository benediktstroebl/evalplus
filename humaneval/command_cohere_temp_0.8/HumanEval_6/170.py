```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()')[':()+'], '))':
        stack = [0]
        for c in s:
            if c == opener:
                stack.append(stack[-1] + 1)
            elif c == Closer:
                stack.pop()
        result.append(stack[-1])
    return result
```
The function processes each group of parentheses separately and uses a stack to keep track of the current nesting level. The `zip('(()')[':()+']` creates iterators `opener` and `Closer` that simulate opening and closing parentheses. It iterates through the characters of `s` and increments or decrements the nesting level based on whether the character is an opener or Closer. Finally, it appends the deepest nesting level for each group to the result list.