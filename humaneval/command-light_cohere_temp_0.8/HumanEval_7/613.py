Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
Do you require any additional assistance with code implementation or debugging?