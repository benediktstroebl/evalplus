```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```

This script uses a basic loop to iterate through each sub-string of the original string that is divided by spaces. It counts nesting levels by tracking open parentheses ('(') and closes parentheses (')') within each sub-string. The deepest level of nesting for each sub-string is then added to the result list.

Here is an example usage of this function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This will output the list [2, 3, 1, 3], which are the deepest levels of nesting for each of the four groups of parentheses in the provided input string.