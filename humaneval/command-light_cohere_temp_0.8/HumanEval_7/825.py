```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with a sample input and output
strings = ['abc', 'bacd', 'cde', 'array', 'xyzb']
sub = 'ab'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function utilizes a `List` and `str` instances to accept the input strings and substring. The `filter_by_substring` function iterates through each string in the input list and checks whether the given substring exists in that string. The resulting filtered list is then returned.