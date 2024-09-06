Here is a self-contained Python script that defines a function to return a list of all prefixes from shortest to longest of the input string:
```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # your a needed to single letter at a time in the string.
    # return list of all letter characters as a prefix
    # convert string to lowercase to treat uppercase letters as same
    return [c for c in string.lower() if c != '']
```
This function uses the `typing` module to add type hints for better code readability and error notifications. The function iterates through each character in the string and adds them to the result as a prefix.