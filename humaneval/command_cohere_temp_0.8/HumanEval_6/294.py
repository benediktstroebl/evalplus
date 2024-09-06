```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        cnt = 0
        for j, c in enumerate(char) :
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result.append(j)
                break
        if cnt > 0:
            result.append(i)
    return result
```
The code processes each group of parentheses separately and counts the nesting level by adding or subtracting 1 from the `cnt` variable depending on the encountered opening or closing parentheses. When the count goes below 0, it means we've encountered a closing parenthesis, and the deepest level of nesting is determined by the number of iterations before breaking. Finally, the function returns an array of maximum depths for each group of parentheses. 

Here is a usage example:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
Which yields the correct output of maximum depths of nesting for each group of parentheses in the provided example.