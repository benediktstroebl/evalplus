```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1) if char.startswith('a')]
``` 
This Python function iterates through each character of a string and returns a list of all prefixes from shortest to longest, where each prefix starts with the character 'a'.