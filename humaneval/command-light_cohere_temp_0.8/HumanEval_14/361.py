```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']
test_cases = [
    'abc', 
    '123', 
    '#!#', 
    '!@#a'
] 

# Test the function
for test in test_cases:
    actual = all_prefixes(test)
    assert actual == ['#', '', '1', '3', '.']
    print(f"Test {test} passed.")
```