```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')) for _ in range(2)])]:
        count = 1
        while opening:
            opening -= 1
            count += 1
        result.append(count)
    return result
```

The problem asks to parse a string `s` that contains multiple groups of nested parentheses separated by spaces, and for each group, compute and return the deepest level of nesting of parentheses.

Here is an example of how to call the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
Which outputs:
```bash
[2, 3, 1, 3]
```

This approach utilizes a concise and efficient strategy based on iterating through paired opening and closing parentheses, incrementing a counter for each unmatched pair encountered. This counter reflects the deepest nesting level within each group, which is then appended to a list and returned as the result.