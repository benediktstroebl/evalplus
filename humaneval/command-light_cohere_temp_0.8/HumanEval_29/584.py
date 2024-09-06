```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases for the function
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'

# Function call and test
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']

# Test case 2
strings = ['hello world', 'hello']
prefix = 'x'

result = filter_by_prefix(strings, prefix)
print(result)  # Output: []
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It then applies this test cases to verify the functionality of the function, successfully printing the expected output.