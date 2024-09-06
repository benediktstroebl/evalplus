```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        count = 0
        nesting_level = 0
        unbalanced = 0
        for char in bracket_str:
            if char == '(':
                count += 1
                unbalanced += 1
            elif char == ')':
                count -= 1
                unbalanced -= 1
                if count < 0:
                    unbalanced += 1
            nesting_level = max(nesting_level, unbalanced)
        result.append(nesting_level)
    return result
```

To use this function, you can call it with a string containing nested parentheses, and it will return a list of the deepest level of nesting for each group of parentheses. Here is an example:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```
This will output:
```bash
[2, 3, 1, 3]
```

The provided example in the markdown code block will print the following:
```bash
[2, 3, 1, 3]
```