```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join([char for char in string if char != ' ']) for char in string] + [string]
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It uses a strategy of iterating over each character in the string and filtering out spaces using a generator expression.