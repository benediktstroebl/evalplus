Here is a self-contained Python script that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.replace(c) for p,c in zip(''.join(s.split(') +')) if c.isspace('(')]
```

This script defines a function, `separate_paren_groups`, which takes a string `s` as input and returns a list of strings, each separated from its parent by an unclosed '(')'. The function uses the `zip` function to iterate through the string, and uses a list comprehension to extract each parent-child pair. The function also uses the strings `(''.join(s.split(') +`)) to account for spaces and ensure only the open parentheses are kept.