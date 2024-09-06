```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '']
test_data = {
    'abc': ['a', 'ab', 'abc'],
    'hello': ['el'],
    'world': ['rld'],
    '!' : ['!']
}
test_cases = [('string', expected) for _, (string, expected) in test_data.  ]
 print('Test Cases:')
for case in test_cases:
    print(f'{case[0]}: { {case[1]}}')
print()

for string, expected in test_data. print print(f'Received {string}: Expected {expected}')
for string, expected in test_cases:
    actual_result = all_prefixes(string)
    print(f'{string} -> {actual_result}: {expected}')
```