```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']
test_data = [
    'abc', '', 'aa', 'a', 'ab', 'abc', 'aab', '!'
  ]
  assert all_prefixes(''.join() == test_data, 'Failures.'
print('All prefixes passed tests.')
```