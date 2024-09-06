```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in a list of strings.
    """
    def compare_length(a: str, b: str) -> bool:
        return len(a) > len(b)
    return max(strings, key=compare_length)
strings = ['a', 'bb', 'ccc']
longest_string = max(strings, key=compare_length)
print(longest_string)
```