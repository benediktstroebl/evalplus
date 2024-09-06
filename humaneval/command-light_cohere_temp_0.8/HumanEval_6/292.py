```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    groups = []

    for c in s:
        if c == '(':
            stack.append(opening_level)
            opening_level += 1
        groups.append(stack.pop())
        open()
        final_level = stack.append(opening_level)
        stack.append(c)

    return groups
```

This function uses a stack to track levels of opening parentheses, and a counter to track the nesting level. It then iterates over each input string character by character, appending characters to the stack if they are parentheses. The function also adds the opening level for each new group of parentheses.

Finally, the function returns a list of integers, where the integer at index i is the depth of the deepest nesting of parentheses starting at index i.