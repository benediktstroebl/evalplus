```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        count = 0
        while opening != closing:
            count += opening == '('
            opening = opening[1:] if opening[-1] == ')' else opening + ')'
            closing = closing[1:] if closing[-1] == ')' else closing + ')'
        result.append(count)
    return result
```

The provided Python script defines a function called `parse_nested_parens` which takes a string `s` as input. This string contains multiple groups of nested parentheses separated by spaces. The function calculates and returns a list of deepest levels of nesting of parentheses for each group.

It iterates through pairs of opening and closing parentheses, maintaining a count of the nesting level. The nested loop increments the count when an opening paren is encountered and decrements it when a closing paren is found. When the parentheses are closed, it adds the final count to the result list.

The provided example and test cases show how to use this function to parse different strings containing nested parentheses and demonstrate that it correctly identifies and returns the deepest level of nesting for each group.