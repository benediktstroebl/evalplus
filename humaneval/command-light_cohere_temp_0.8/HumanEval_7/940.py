```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "Hello, World!", "abc", "!", "Everything is ok"]
substrings = ["a", "Hello", "World"]

print("Test case 1: ", end="append)
print(filter_by_substring(strings, substrings))  # Output: ['abc', 'Hello, World']

print("Test case 2: ", end="append)
print(filter_by_substring(strings, substrings))  # Output: ['abc']

print("Test case 3: ", end="append)
print(filter_by_substring(strings, "ok"))  # Output: ['abc', '!']

print("Test case 4: ", end="append)
print(filter_by_substring([ Gaston ], "Wun"))  # Output: []
```
The provided Python script defines a function `filter_by_substring` that filters a list of strings based on whether the given substring is present in each string. The function iterates through each string in the list and checks if the given substring exists. 

The script then passes the function with several test cases, and the output is printed to the console. 

Please note that the function is self-contained and does not require any external functions or modules.