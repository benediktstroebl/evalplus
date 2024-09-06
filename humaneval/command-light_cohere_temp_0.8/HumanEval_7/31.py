```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hea', 'hey']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output ['abc', 'bacd', 'array']
``` 
This script defines a function `filter_by_substring` that filters an input list of strings based on a given substring.  It uses a important technique to iterate through the input list and checks whether each string contains the given substring.