```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join([char for char in s if s != '' and char <=128 and char >= 92][:2] for s in string)
for x in ['']:
    test_case = [''.join([x for char in s if s != '' and char <= 128 and char >= 92][:2] for s in 'abc'])
    if test_case != all_prefixes(test_case):
        raise ValueError('Test failed')
```