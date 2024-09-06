```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()') + s + '())':
        stack = [0]
        level = 0
        while opener in Closer:
            stack.append(level)
            if opener == Closer:
                break
            level += 1
        result.append(stack.pop())
    return result
``` 

This code utilizes a generator expression `'(()' + s + '()))'` to simulate the nested structure of parentheses, sending a list of `levels` for each closing parenthesis to the `result` list. The logic of the `stack` and `level` counter figures out the deepest level of each group. Finally, the list is reversed to get the correct order and the largest depth of each group is returned. 

This approach allows the solution to accomplish the problem efficiently and elegantly.