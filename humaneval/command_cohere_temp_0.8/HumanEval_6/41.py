```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for parentheses in s.split():
        counter = 0
        nested = 0
        for char in parentheses:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                nested = max(nested, counter)
        result.append(nested)
    return result
```
The function iterates over each group of parentheses, maintains a counter to track the overall enclosure, and updates the `nested` variable to return the maximum depth of nesting every time a closing parenthesis is encountered. The final result is a list of the deepest nesting level for each group of parentheses.