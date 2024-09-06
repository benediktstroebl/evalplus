```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        level = 0
        unbalanced = False
        for c in chunk:
            if c == '(':
                level += 1
            elif c == ')':
                if unbalanced:
                    level -= 1
                else:
                    level -= 1
                    unbalanced = True
            result.append(level)
    return result
```
The logic is straightforward. We iterate through each character in the string and whenever we encounter a '(' character we increment the level, and whenever we encounter a ')' character we decrement the level. When the level reaches 0 and there are no more '('' characters, the loop exits and we add the level to our result list. To handle multiple groups of parentheses separated by spaces, we first split the input string into list of chunks and then process each chunk separately. And that's it. Hope this helps! Let me know if you have any concerns.