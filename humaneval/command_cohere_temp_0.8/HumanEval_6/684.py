```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        i = 0
        while i < len(opening) or i < len(closing):
            if opening[i] == '(':
                depth += 1
                nested += 1
            elif closing[i] == ')':
                nested -= 1
                if not nested:
                    result.append(depth)
                    break
            i += 1
    return result
```

The `parse_nested_parens` function takes a string `s` containing nested parentheses separated by spaces as input. It iterates through the openings and closings of parentheses using `zip(*[iter(s.split())] * 2)`, maintaining a `depth` and `nested` counter to track the current depth and the number of unopened parentheses respectively. The loop continues until all parentheses are closed, at which point the current depth is added to the `result` list, and the next iteration of the loop begins. The final result is a list representing the maximum depth of nesting for each group of parentheses.