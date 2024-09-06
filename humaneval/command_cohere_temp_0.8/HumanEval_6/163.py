```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for separated_string in s.split():
        string = ''.join(separated_string.split())
        count = 0
        depth = 0
        nonlocal result
        i = 0
        while i < len(string):
            if string[i] == '(':
                count += 1
                depth = max(depth, count)
            elif string[i] == ')':
                count -= 1
            i += 1
        result.append(depth)
    return result
```

The code uses a simple iterative approach to parse the strings. It counts the number of open parentheses encountered at every step and uses this number to keep track of the current depth of nesting. The maximum depth attained during the iteration is used to generate the final result list.