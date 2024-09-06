```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "falaf", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print("Result:", result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function called **filter_by_substring** that takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring. 

In the code, we have a test case with a list of strings **strings** and a substring **substring**. The code then calls the function **filter_by_substring** with these inputs and prints the result, which should be the list of strings from the input list that contain the given substring.