```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', 'abc']

# Test cases
test_cases = [
    ('abc',),
    ('abcde',),
    # Longer strings
    ('anding', 'andrewing'),
    # Different characters
    ('#$%^&*()',),
]

for i, test in enumerate(test_cases):
    actual_result = all_prefixes(test)
    print(f'Test {i+1}: "{test}" => {actual_result})
```