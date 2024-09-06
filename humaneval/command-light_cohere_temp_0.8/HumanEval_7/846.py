```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with sample inputs and outputs
strings = ['abc', 'bacd', 'cde', 'array', 'text']
substr = 'a'

print("Test 1 Result:", filter_by_substring(strings, substring))
print()

print("Test 2 Result:", filter_by_substring(strings, 'ba'))
print()

print("Test 3 Result:", filter_by_substring(strings, 'cde'))
print()

print("Test 4 Result:", filter_by_substring(strings, 'arX'))
```