Here is a self-contained Python script that includes the function filter_by_substring, which is designed to solve the problem of filtering markdown code blocks based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x.string.joinf is