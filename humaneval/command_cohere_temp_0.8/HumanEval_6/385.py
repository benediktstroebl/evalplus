```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')) for _ in '03']):
        result.append(len(opening))
    return result
```

The Python script solves the problem using a clever approach. It iterates through the opened and closed parentheses of each separated string component using zip and replaces(' ', '') to remove any spaces and closing parentheses ')' to allow them to be used as counters for each iteration. By doing so, it determines the depth of each opening parentheses in each string section and appends the deepest levels to the result list.