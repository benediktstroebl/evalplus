```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [substr for substr in string[i:].split() for i in range(2)]

# Test the function with a string containing more prefixes
test_string = 'acbab'
result = all_prefixes(test_string)
print(result)
```