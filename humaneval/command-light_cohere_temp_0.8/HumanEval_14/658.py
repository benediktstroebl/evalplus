```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). minimum(map(str.lower, string)) for i, char in string if i > 0 and char.lower() != ' '']
```
This code implements a function that returns a list of all prefixes from the shortest to the longest of the input string. It uses the map function to iterate over each character in the string, and the filter function to only keep the characters that are not spaces.