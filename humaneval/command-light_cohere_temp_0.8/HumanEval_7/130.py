```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function takes a list of strings and a substring as inputs. It uses the `contains` to check if each string in the input list contains the given substring.