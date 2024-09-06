```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
            elif c == closer:
                if not stack or opener == stack.pop():
                    level += 1
                else:
                    level -= 1
            result.append(level)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each of the groups separated by spaces.

The function iterates through the input string using a zip with '([{' as openers and ')]}' as closers, maintaining a stack of recently encountered openers, and counting the deepest nesting level of parentheses. It iterates through the string and increments the level when an opener is encountered and the top of the stack is a closer, and vice-versa. The result is a list of these levels for each group in the input string.