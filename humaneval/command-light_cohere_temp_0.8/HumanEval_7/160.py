```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]


#Test cases
test_strings = ['abc', 'bacd', 'cde', 'array', 'hello']
test_substring = 'a'
result = filter_by_substring(test_strings, test_substring)
print(result)
```