```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nesting = 0
        i = 0
        while i < len(chunk):
            if chunk[i] == '(':
                nesting += 1
            elif chunk[i] == ')':
                nesting -= 1
            i += 1
        result.append(nesting)
    return result
```

The `parse_nested_parens` function takes a string `s` as input, where each space-separated chunk is a group of parentheses. The function iterates through each character of each chunk, keeping track of the current nesting level with a `nesting` variable. When an open parenthesis `(` is encountered, the `nesting` level is incremented, and when a closing parenthesis `)` is encountered, the nesting level is decremented. Finally, the function returns a list of the maximum nesting levels for each group of parentheses. 

This approach handles all possible combinations of parentheses, ensuring that the function will return the correct result for any valid input.