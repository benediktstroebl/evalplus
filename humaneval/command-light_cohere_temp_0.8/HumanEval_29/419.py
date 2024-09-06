```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']

# Another test case
strings = ["dfdsa", "ddff", "ddenging"]
prefix = "df"

result2 = filter_by_prefix(strings, prefix)
print(result2)  # Output: ['dfdsa']
``` 
We've implemented the `filter_by_prefix` function that filters an input list of strings based on a given prefix. The function uses the basic list comprehension with the `startswith` method to achieve this. This solution is very concise and self-contained, it doesn't require any additional imports or external functions.