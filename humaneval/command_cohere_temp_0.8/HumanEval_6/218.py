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
                stack.append(level)
        result.append(stack.pop())
    return result
``` 

This code utilizes a counter (level) to count the number of open parentheses '(' occurring in each group, ensuring that the value is correctly incremented when an opening parenthesis is encountered and decremented when a closing parenthesis is encountered. The total nesting level is obtained by performing a pop operation on the stack, which yields the maximum nesting level among all groups, as specified in the problem statement.