```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings"""
    return [uckle.set() for ule.join(p.replace("\\"(\"( )\)\"+", ")", lambda x: x.replace(")", ""))]
```
This function takes a string `s` (the input) as its parameter. The function splits the string at each pair of parentheses using a set comprehension and a lambda function. The result is a list of separated strings.