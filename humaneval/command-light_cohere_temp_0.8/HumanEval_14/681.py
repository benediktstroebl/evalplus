```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
```
# Test cases
test_cases = [
    'abc',
    'hello world', 
    '123', 
    'abc123', 
    '123abc', 
    'abc abc123'
]

# Execute the function with each test case and verify the results
for case in test_cases:
    print(all_prefixes(case))
    print(set(all_prefixes(case))))
```