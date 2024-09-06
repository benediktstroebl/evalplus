```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], '())':
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.pop()
        result.append(stack[-1])
    return result
```
The function iterates through each character of the input string `s`. When an open parenthesis is encountered, the nesting level is incremented and when a closing parenthesis is encountered, the nesting level is decremented. The final nesting level is stored in the result list.

To achieve this, the function uses two iterators:
1. `('(()')[::-1]`) - This iterator reverses the string '(()' which essentially gives us closing parenthesis first, followed by opening parenthesis and then closing parenthesis again.
2. `zip('(()')[::-1], '())' - This iterator zips the above iterator with another string '())' which gives the sequence of (open, close) pairs.

This approach ensures that for each opening parenthesis encountered, there is a matching closing parenthesis. When an opening parenthesis is encountered, the nesting level is incremented, and when a closing parenthesis is encountered, the nesting level is decremented. The maximum nesting level of each group is maintained in the `stack` list and finally stored in the `result` list.