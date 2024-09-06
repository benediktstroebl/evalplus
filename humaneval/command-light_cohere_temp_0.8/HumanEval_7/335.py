```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

#Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters an input list of strings based on whether the substring is present in any element of the list. 
The function utilizes a list comprehension to iterate over the strings and returns a new list containing only the strings that contain the given substring. 

The script also includes test cases that pass the function's execution, and the function correctly filters the strings based on the given substring.