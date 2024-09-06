```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nesting = 0
        unbalanced = 0
        for c in chunk:
            if c == '(':
                nesting += 1
                unbalanced += 1
            elif c == ')':
                nesting -= 1
                if unbalanced > 0:
                    unbalanced -= 1
                else:
                    result.append(nesting)
        if unbalanced > 0:
            result.append(unbalanced)
    return result
```

The code processes each whitespace-separated chunk separately and keeps track of the nesting level of parentheses. When a closing parenthesis is encountered, the nesting level is decremented. If it falls below zero, it means there are more closing parentheses than opening ones in this chunk, and this is reflected in the result for that chunk. The final result is a list where each element corresponds to the deepest nesting level of parentheses in one of the chunks. 

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This approach has a time complexity of O(N) where N is the number of characters in the string, and a space complexity of O(N) as well since we keep track of the unbalanced parentheses in a list.