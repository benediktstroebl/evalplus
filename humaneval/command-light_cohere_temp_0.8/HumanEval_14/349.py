```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i, char in enumerate(string, 1) if char.isalpha() oral:
        # We need to account for the case where an alphabet
        # is the entire input string.
        if char == string[-1]:
            return []
    return [char] + all_prefixes(string[:i])
def all_alphabet(string: str) -> List[str]:
    return [c for c in string if c.isalpha()]
isalpha()
```

The all_prefixes function will return a list of all prefixes from shortest to longest of the input string, using the list comprehension technique and a counter function. The function will first check if the last character of the string is an alphabet, if it is, it returns an empty list. If it is not, it will return the current character and then use the all_prefixes function to get all the prefixes of the input string starting from that character.