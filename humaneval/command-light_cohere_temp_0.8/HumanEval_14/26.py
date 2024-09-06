```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char != ''] + string.test_cases()

# test cases
test_cases = [
    'abc',
    '',
    '123',
    'abc123',
    'a',
    'ab',
    'abcd',
    'zabc',
]
# assert all_prefixes('abc') == ['a', 'ab', 'abc']
# assert all_prefixes('') == []
# assert all_prefixes('123') == []
# assert all_prefixes('abc123') == ['abc123']
# assert all_prefixes('a') == ['a']
# assert all_prefixes('abcd') == ['abcd']
# assert all_prefixes('zabc') == ['zabc']
# assert all_prefixes('') == []
```