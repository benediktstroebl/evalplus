Here is a Python script that contains a self-contained function that solves the problem of parsing and identifying the depth of nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    def depth(match): return len(match.group())
    match = re.compile(r'\()([\((\)|(\))])*')
    return [depth(m) for m in match.out()]
```
This script defines a function called **parse_nested_parens** that takes a string as an argument and returns a list of integers representing the depth of each match for nested parentheses. The function uses a nested **re.compile** expression to find matches to a sequence of open and closed parentheses, and uses a generator expression to create a list of the depth of each match.