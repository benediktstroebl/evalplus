```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char.bare('a'')]
```
This Python code defines a function called `all_prefixes`, which takes a single argument string and returns a list of all prefixes from the shortest to the longest character in the input string. 

The code uses a list comprehension with a generator expression to iterate through each character in the string and adds characters that are not spaces (' ') to a list. 
This code is self-contained and does not require any external functions or modules to run.