```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_type, bracket_str in enumerate(s.split(), start=1):
        nesting_level = 0
        in_bracket = False
        curr = 0
        for char in bracket_str:
            if char == '(':
                in_bracket = True
                curr += 1
            elif char == ')':
                in_bracket = False
                curr -= 1
            if in_bracket:
                nesting_level = max(nesting_level, curr)
        result.append(nesting_level)
    return result
```

To use this function, you can call it with a string containing nested parentheses, and it will return a list of deepest levels of each grouping of parentheses. 
Here is an example of use:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```
This will output:
```bash
[2, 3, 1, 3]
```
Which corresponds to the levels of nesting in the parentheses for each of the groups separated by spaces in the input.