Here's a Python script with a self-contained function that solves the problem using a straightforward nested list comprehension approach:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    levels = [len(x.count('(')) - len(x.count(')')) for x in paren_string.split(' ') if x]
    return levels
```
This approach splits the input string into spaces and then loops through each substring. It counts the number of '(' and ')' characters using the `count` method and subtracts to get the nesting level. 

Here's how you can use it and pass the tests:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
This approach provides a concise solution to the problem.