```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '']

# Test the function
string = "abc"
test_case = all_prefixes(string)
print(test_case)  # Output: ['a', 'ab', 'abc']
```