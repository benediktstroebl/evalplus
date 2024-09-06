```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Testing the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Expected output ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses the particular list comprehension to iterate over the strings and elements in the list. The function then returns a filtered list containing only the strings that contain the given substring. 

The code then passes tests by creating a test strings list and substring, and calling the `filter_by_substring` function with these inputs. The expected output of the resulting list should be ['abc', 'bacd', 'array'], which are the strings that contain the substring 'a'.