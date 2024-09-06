```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with some inputs and expected outputs
strings = ["abc", "bacd", "cde", "array", "hello", "world!" ]
substr = "a" 

print("Test 1: ", end=" ")
print(filter_by_substring(strings, substring))
print("====" end=" ")
print(strings.

strings = ["abc", "bacd", "cde", "array", "hello", "world!"]
substr = "d" 

print("Test 2: ", end=" ")
print(filter_by_substring(strings, substring))
print("====" end=" ")
print(strings)
```

This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a list comprehension to iterate through the input strings and returns only the strings that contain the given substring. 

The script then passes the function with two sets of strings and the expected substring, and the output is printed to verify the function's correctness.