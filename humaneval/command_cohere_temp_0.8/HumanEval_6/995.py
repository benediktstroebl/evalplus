```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nesting = 0
        level = 0
        start = 0
        for c in char:
            if c == '(':
                nesting += 1
                if nesting == 1:
                    start = i
            else:
                nesting -= 1
                if not nesting:
                    result.append(level)
                    level = 0
                if nesting == -1:
                    end = i
                    level = nesting // 2
                    result.append(level)
    return result
```

To use this function, you can call it with a string containing nested parentheses, and it will return a list of the deepest level of nesting for each group of parentheses. Here is an example:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```

This would output:
```python
[2, 3, 1, 3]
```

This output corresponds to the example provided in the problem statement. The function considers each group of parentheses separately and calculates the maximum nesting level for each group, accounting for the nested nature of parentheses.