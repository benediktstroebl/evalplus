```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in reversed(list(map(len, s.split()))):
        if not bracket_level:
            break
        result.append(bracket_level)
    return result
```

The reversed `map` function splits the input string into different groups of parentheses and calculates the length of each group i.e. the nesting level. The maximum nesting level of any group is added to the `result` list. The list is then returned from the function. 

**NOTE:** The code assumes that the number of parentheses groups is spaced out with spaces, as shown in the example given. If the groups are separated by other characters or have different structures, the code may not provide the correct results.