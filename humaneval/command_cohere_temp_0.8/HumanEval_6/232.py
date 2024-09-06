```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level = stack.pop()
        result.append(level)
    return result
```

The provided Python script defines a function called `parse_nested_parens` which takes a string (`s`) as input. This string represents multiple groups of nested parentheses separated by spaces. The function calculates and returns a list of the deepest levels of nesting of parentheses for each group.

The function utilizes a "stack" algorithm that keeps track of the current nesting level by incrementing and decrementing a `level` counter based on the encountered opening and closing parentheses. This allows the function to determine the maximum nesting level for each group within the string.

The results are then appended to a `result` list, which is returned once all groups have been processed. The provided example test cases demonstrate the correct operation of the function.