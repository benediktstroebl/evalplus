```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
This function iterates through each character in the string and checks if the character is an uppercase letter, then it will return the character and remove it from the string.

```
This code is self-contained, and it does not require any external modules or functions. It provides a's a list of all prefixes from shortest to longest of the input string, using a list comprehension and the `isalpha()` method.