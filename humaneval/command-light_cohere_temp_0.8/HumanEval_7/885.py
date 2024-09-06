```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function with different inputs
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Expected output ['abc', 'bacd', 'array']
``` 
The provided code defines a function **`filter_by_substring`** that filters a list of strings for a given substring. The function uses a list comprehension to iterate over each string in the input list. It checks if the string contains the given substring using the in-built **`contains`** method.