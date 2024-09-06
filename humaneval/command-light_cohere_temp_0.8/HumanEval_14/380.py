```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join()[i] for i, char in enumerate(string) if char.join()]
```

# Test cases
test_strs = ['abc', 'hello', 'world', '', '1234']
test_results = [all_prefixes(test_str) for test_str in test_strs]

print("Test Results:", test_results)
```