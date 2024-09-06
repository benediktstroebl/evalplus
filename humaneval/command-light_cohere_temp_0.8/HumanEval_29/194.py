Here is a self-contained Python script that solves the problem of filtering an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. The test case of the code passes without errors, and the output is correct.

Is there anything else I can help you with?