```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
test_strings = ["abc", "bacd", "cde", "array", "hello"]
test_substring = "a"

result = filter_by_substring(test_strings, test_substring)
print(result)

if len(result) != 4:
    raise ValueError("filter_by_substring() did not return the expected result")
``` 
This Python code defines a function filter_by_substring that filters a list of strings for a given substring. The function utilizes a list comprehension to iterate over each string in the input list. The condition checks if the string's characters match the given substring, if so, it is included in the resulting list.