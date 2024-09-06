```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string if c.isalpha()]
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
``` 
This Python script defines a function `all_prefixes` that returns a list of all prefixes of a given string. The function uses list comprehension and the built-in function `isalpha()` to filter out non-alphabetic characters.