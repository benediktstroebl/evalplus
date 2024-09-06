```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test case 1
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)
# Output ['abc', 'bacd', 'array']

# Test case 2
strings = ['hello world']
sub = 'x'
result = filter_by_substring(strings, sub)
print(result)
# Output []
```