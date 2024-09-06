```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join[i for i, c in enumerate(string) if c.isalpha()] + string[1:]
```

This code defines a function called all_prefixes that takes a string as input and returns a list of all prefixes from shortest to longest of the input string. It uses the particular test and a list comprehension with the enumerate function to iterate over each character in the string. The condition is whether the character is an alphabet character (represented by c.isalpha()), and the string is a string containing only letters, so the list comprehension generates all prefixes of the string.