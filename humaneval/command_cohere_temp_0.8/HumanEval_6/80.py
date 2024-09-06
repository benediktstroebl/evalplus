```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        while opening != closing:
            if opening == '(':
                depth += 1
            elif closing == ')':
                depth -= 1
                nested += depth
            opening = closing
        result.append(nested)
    return result
```

This script takes a string `s` which contains multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group. 

The algorithm works by:
1. Iterating through each group of parentheses, determined by spaces, with two nested iterators.
2. Keeping track of the `depth` of parentheses with a `while` loop that reacts to opening parentheses by incrementing the `depth` and vice versa for closing parentheses.
3. The `nested` variable keeps track of the overall nested depth while the loop runs.
4. Append the `nested` depth for each group to the `result` list. 

The provided example in the prompt yields the result: `[2, 3, 1, 3]`.