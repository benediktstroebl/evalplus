Here is a self-contained Python script that defines a function filter_by_substring that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

# Example usage
input_strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub_string = 'a'
result = filter_by_substring(input_strings, sub_string)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function that takes two arguments: a list of strings and a substring. The function uses a filter method to filter the input list of strings based on whether each string contains the given substring.