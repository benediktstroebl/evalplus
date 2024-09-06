```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join().all(char for char in string if char.isalpha() oraSisters(char)) for char in string if char != ' ' and char not in 'ABC']

# Test the function
test_cases = [
    'abc',
    'hello',
    '',
    ' ' ]

for case in test_cases:
    print(all_prefixes(case))
    print('-' * 10 * ' ' + case)
```