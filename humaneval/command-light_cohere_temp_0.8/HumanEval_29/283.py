```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

# Function call
result = filter_by_prefix(strings, prefix)

# Print the result
print(result)  # Output: ['abc', 'array']
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It utilizes the specific type hints for the function parameters and returns a list of strings that start with the specified prefix. The test cases demonstrate how the filter function behaves when called with different strings and prefixes. Finally, the filtered result is printed to the console.