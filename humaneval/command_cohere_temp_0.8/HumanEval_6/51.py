```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')')[::-1]:
        stack = [0]
        curr = 0
        for ch in s:
            if ch == opener:
                curr += 1
            elif ch == closer:
                curr -= 1
                stack.append(curr)
        result.append(stack.pop())
    return result
```

The algorithm works by iterating through each character in the string `s`. When the character is an opening parenthesis, the nesting level `curr` is incremented. When it encounters a closing parenthesis, the nesting level is decremented. The maximum nesting level of each group is added to the `result` list.