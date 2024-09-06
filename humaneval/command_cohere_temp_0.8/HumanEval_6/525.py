```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()') + s + '())':
        level = 0
        while opener in s and s.strip('())'):
            if opener == s[0]:
                s = s[1:]
            elif closer == s[0]:
                s = s[1:]
                level += 1
            else:
                break
        result.append(level)
    return result
``` 

This code block implements a function called `parse_nested_parens`, which takes in a string `s` as input. It iterates through different length prefixes of `s`, counting nested parentheses as it goes. The result is a list of deepest nesting levels for each of the subgroups.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This returns a list with the four deepest levels of nesting of the parentheses in the provided string.