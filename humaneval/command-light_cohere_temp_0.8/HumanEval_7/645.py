```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 strings: List[str] = ['abc', 'bacd', 'cde', 'array', 'text', 'tesc']
    substring: str = 'a'
    return strings if substring in strings else []
 ```