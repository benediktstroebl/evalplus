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

The algorithm uses the fact that the maximum depth of nesting of parentheses in a string of length L is O(L). So we iterate through the string just once, maintaining a `stack` of the depths of open parentheses encountered so far. Each time we encounter an open parentheses, we increment the `level` and add it to the `stack`. When we encounter a closing parentheses, we decrement the `level` and pop the top of the stack. The deepest level of nesting of parentheses at the end of the string is then the last element in the `stack`. The zip technique is used to reverse the order of openers and closers as '(()' is reversed to '())'.