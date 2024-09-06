Here's a self-contained Python script that solves the provided problem:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.split('()') if x.count(('()'))]
```

This script defines a function `parse_nested_parens` that takes a string s as input and returns a list of integers. The function splits the strings into list of characters using `s.split('()` method and then checks if each character is either '(' or ')'. The function then uses the `enumer` function to iterate over the list of characters and count the number of '(')'.

This script is a good start and can be used as a base to build upon. It is self- contained and easy to test.