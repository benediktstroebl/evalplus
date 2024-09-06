```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 return []
# Example usage
strings = ["abc", "bacd", "cde", "array", "meatball", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)
```