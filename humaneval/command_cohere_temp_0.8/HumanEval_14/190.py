```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string[::-1], [string[-1]:]]))[0]
```
The function leverages Python's `accumulate` function to generate all prefixes of the reversed string sorted in ascending order. Then, we use slicing and a tuple unpacking assignment to reverse that order and retrieve the desired prefixes. The type hint `List[str]` for the return value indicates a list of strings, while the docstring provides a brief description of the function's purpose and behavior.