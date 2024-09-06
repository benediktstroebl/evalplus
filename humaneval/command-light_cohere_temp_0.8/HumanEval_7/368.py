```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != - -end]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python script defines a function `filter_by_substring` that filters an input list of strings based on the presence of a given substring. The function uses the for each element in the list and checks if the substring is found using the `find()` method. If the substring is not found, the element is not included in the resulting filtered list.