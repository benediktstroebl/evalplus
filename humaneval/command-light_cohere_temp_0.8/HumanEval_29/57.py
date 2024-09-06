```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', 'for', 'array', 'a']
prefix = 'for'
test_filter = [('Should return list with', 'this string starts with', 'prefix: %s', 'and has %d' % (len(prefix))) for _,string, prefix in zip(strings, [prefix for _ in strings]))
print('Unit test results:')
for test in test_filter:
    print(test)
```