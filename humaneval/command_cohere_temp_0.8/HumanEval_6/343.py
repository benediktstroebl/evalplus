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

This code defines a function `parse_nested_parens` that takes a string `s` containing nested parentheses as input. It iterates through the string, tracking the opening and closing parentheses simultaneously using two separate iterators. It maintains a `count` variable that keeps track of the number of opening parentheses encountered before encountering the corresponding closing parenthesis. Once the closing parenthesis is found, it updates the count accordingly. The process repeats until all parentheses are processed. Finally, it returns a list of counts, representing the maximum nesting depth for each group of parentheses.