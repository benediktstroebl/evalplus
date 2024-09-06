```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i,c in enumerate(s.split(',')) if c=='(']
```
This function takes a string `s` as input and uses a list comprehension to iterate over the characters in the string. It then uses the `enumerize` function to iterate over the characters in the string and returns a list of the indexes of the parentheses encountered.