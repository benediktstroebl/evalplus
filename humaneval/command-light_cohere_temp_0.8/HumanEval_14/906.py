```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix else ''] + [string]

# Test case: Simple string with all prefixes
test_case = 'abc'
result = all_prefixes(test_case)
print(result)  # Expected output: ['a', 'ab', 'abc']
```
This script defines a function called **`all_prefixes`** that returns a list of all prefixes of a given string, starting from the shortest to the longest, including the original string. It then applies this string to the function and prints the result, which should match the expected output.