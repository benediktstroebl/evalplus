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

The approach employed by the function `parse_nested_parens` is to loop over each of the parentheses group in the input separated by spaces and maintain a stack of the number of parentheses at each level. The loop continues until an opener is found that matches a closer in the stack or an unmatched opener is encountered. Subsequently, the stack is traversed to obtain the maximum depth of nesting for each group, which is then appended to the results list.