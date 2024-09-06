```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')['::-1], '())'['::-1]:
        stack = [0]
        curr = 0
        for ch in s:
            if ch == opener:
                curr += 1
            elif ch == closer:
                curr -= 1
                stack.append(curr)
            else:
                continue
        result.append(stack.pop())
    return result
```

The algorithm utilizes a nested list `stack` to keep track of the incrementing and decrementing parentheses encountered during iteration through the input string `s`. The `zip('(()')['::-1], '())'['::-1]` trick is used to reverse the order of openers and closers and also to remove duplicates, so that for each opener we have a corresponding closer. The `result` list is populated with the maximum depth of nesting for each group of parentheses encountered.