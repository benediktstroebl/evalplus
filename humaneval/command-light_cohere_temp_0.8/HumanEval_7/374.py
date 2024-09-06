```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  
``` 
This code defines a function called **filter_by_substring** that filters a list of strings for a given substring. It uses the the the filtering is achieved using a list comprehension, where each string is checked for the presence of the given substring. The output is then the list of strings that contain the substring. 

The test code creates an example with a list of strings and a substring, and then calls the function with those values. It prints the expected result, which is the list of strings that contain the substring.