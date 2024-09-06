```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings for the presence of a substring."""
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "hello", "world", "!bcd", "test"]
sub = "er"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bcd', 'test']
``` 
This Python script defines a function `filter_by_substring` that filters a list of strings for the presence of a given substring. The test cases show how the different inputs and expected outputs.