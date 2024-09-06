```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function aims to parse and return the deepest level of nesting for a string of parentheses.
    :param s: The string to parse.
    :return: a list of positions of closing parentheses in the string, in descending order of nesting
    """
    return [pos for pos in reversed(map(lambda x: x == ')', s))
```
Do you require any assistance with other Python-related tasks?