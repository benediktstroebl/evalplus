```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.split(' ') '.join(sorted(filter(str.split(' ')[0])))

# Test cases
test_cases = [
    'three one five',
    'six three eight',
    'zero seven nine',
    'four six nine',
    'five eight six'
]

for test_case in test_cases:
    actual = sort_numbers(test_case)
    assert actual == 'one three five', f'[Test case: {actual}] {error}'
```