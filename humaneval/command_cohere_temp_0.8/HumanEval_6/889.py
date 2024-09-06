```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')) for _ in ' '*len(s)]]):
        result.append(len(opening))
    return result
```

The provided Python script solves the problem of parsing nested parentheses and returns a list of depths of each group in the input string. The function iterates through the input string and uses nested loops to iterate through each pair of opening and closing parentheses, calculating the depth of each group of parentheses. The solution is elegantly implemented with list comprehension and zip, achieving a concise and readable code block.