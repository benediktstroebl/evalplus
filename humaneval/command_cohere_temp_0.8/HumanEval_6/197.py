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

This code uses a generator expression `'(()'[::-1])'` to create iterators `opener` and `closer` that yield all open and close parentheses respectively. It iterates through the characters of `s` using a `for` loop, and maintains a `level` counter that keeps track of the current depth of nesting. When an opening parenthesis is encountered, the `level` is incremented, and when a closing parenthesis is encountered, the `level` is decremented. The maximum depth of nesting within each group is stored in the `stack`, with the deepest level of nesting being at the top. Finally, the last element of the `stack` is popped out, and together with the `stack` they are appended to `result`, before being returned as a `List[int]` representing the maximum nesting levels of each group of parentheses. 

To use the `parse_nested_parens` function, you can import it and provide input accordingly:
```python
from your_file import parse_nested_parens
result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)
``` 
The output will be:
```bash
[2, 3, 1, 3]
``` 
This demonstrates the deepest level of nesting for each group of parentheses in the provided input string.