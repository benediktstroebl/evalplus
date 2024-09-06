```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string. string(1) if i.startswith(string)]
```
This Python function, `all_prefixes`, accepts a string `string` as input and returns a list of all prefixes from shortest to longest of the input string. It uses a generating a list comprehension to create a list of prefixes by starting each character from the input string, and checking if the character is the start of the string. This provides all the short and simple solution to the given problem.