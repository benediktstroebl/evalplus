```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "cba", "dog", "Hello", "abc", "hello"]
substring = "o"

# Function call
result = filter_by_substring(strings, substring)

# Print results
print(result)
```