```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "content", "xyzt"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```  This Python code defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function takes two input arguments: `List[str]`, which is a list of strings, and `str`, which is a string to filter. The function uses the string's `in` operation to iterate over the strings in the input list and check if each string contains the given substring. 
The result is a new list that contains only the strings from the input list that contain the specified substring.