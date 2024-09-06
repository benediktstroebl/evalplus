```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        chunk = chunk.replace('(', '').replace(')', '')
        depth = 0
        unbalanced = 0
        for i in range(len(chunk)):
            if chunk[i] == '(':
                depth += 1
                unbalanced += 1
            elif chunk[i] == ')':
                depth -= 1
                unbalanced -= 1
            if depth < 0:
                unbalanced += depth
                depth = 0
        result.append(unbalanced)
    return result
```

The function iterates over each chunk and maintains a `depth` variable that keeps track of the current nestedness of parentheses. For every `(` encountered, the depth is increased and `unbalanced` is increased by 1. For every `)` encountered, the depth is decreased and `unbalanced` is decreased by 1. If at any point the depth becomes negative, it resets it to 0 and adds the absolute value to `unbalanced`. The final output is a list that contains the maximum unbalancedness of each chunk.