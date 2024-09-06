Here is a self-contained Python script that implements the filter_by_substring function, which takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Call the function with test cases
result = filter_by_substring(strings, substring)

# Print the result
print(result)
```

This code defines a function `filter_by_substring` that filters a list of strings, extracting only those that contain a given substring. It uses the … the list comprehension to iterate through all elements in the input strings list, and checks if each element's `substring` attribute is not empty. 

Then, the code passes the test cases and calls the `filter_by_substring` function with the test cases and the given `substring`. The output will be a list containing only the strings that contain the specified substring, which is ['abc', 'bacd', 'array'].