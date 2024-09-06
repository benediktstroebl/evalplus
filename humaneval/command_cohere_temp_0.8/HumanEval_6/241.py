```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a stack to track the depth of nesting for each opening parenthesis encountered. Whenever a closing parenthesis is encountered, its matching opener's depth is added to the stack. Subsequently, the stack is popped when encountering a closing parenthesis without any matching opener. Ultimately, the function returns the list of deepest nesting levels for each group of parentheses. 

To understand the logic better, let's break down the key components:
1. **Zip Function**: The opener and closer arguments to the zip function return iterators of len(opener) and len(closer) respectively. The iterators produced are alternating strings of the opener and closer parentheses. This allows us to iterate over them pairwise in the following loop.
2. **Loop**: In this loop, we iterate over pairs of openers and closers. We use the stack to keep track of the total depth of openers encountered so far. Whenever we encounter an opener we append to the stack, whenever we encounter a closer, we pop from the stack. The top of the stack at the end of the loop will be the deepest level of nesting for the openers encountered.
3. **Result**: The result list is appended with the last value of the stack for each pair of openers and closers iterated. This is the deepest level of nesting for that specific opener/closer pair.