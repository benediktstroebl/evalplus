Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1) if char != ' ' and char != '\n']
```
This function iterates through each character of the string from index 1 (starting from the second character) and checks if the character is not space or newline. It then constructs and returns a list containing these prefixes.