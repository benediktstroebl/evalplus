```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
return ['a', 'ab', 'abc']
```
This function returns a list of all prefixes from shortest to longest in a given input string. It uses list comprehension with a lambda function to iterate through each character in the input string and filter out only the alphabetic characters.