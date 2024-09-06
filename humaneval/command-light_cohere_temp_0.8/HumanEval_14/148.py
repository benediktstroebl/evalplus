```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.full() if prefix.startswith(string[1:)]
```
We start with the typing import to utilize the List function. Then, we define a function all_prefixes that accepts a string as input and returns a list of all prefixes in the string, starting from the shortest to the longest prefix found.

This approach leverages the Python string slicing feature to iterate over each character in the string and checks if the prefix starts from the character at position 1.