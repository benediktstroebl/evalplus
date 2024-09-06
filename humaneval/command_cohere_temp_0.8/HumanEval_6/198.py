```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i, nested = 0, 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            nested = nested + 1 if nested < 0 else 0
        elif char == ')':
            forOpening -= 1
            nested = nested - 1 if nested > 0 else 0
        if forOpening == 0:
            result.append(nested)
            i += 1
            nested = 0
    return result
```

The algorithm is a simple nested loop that iterates over the characters of the input string `s`. To keep track of the opening parentheses, we use `forOpening` and to track the current level of nesting we use `nested`. Whenever we encounter an opening parenthesis, we increment `forOpening` and increment or decrement `nested` depending on its current value. When we encounter a closing parenthesis, we decrement `forOpening` and accordingly adjust `nested`. We reset `nested` to 0 at the beginning of each group and add the current value to our result list.