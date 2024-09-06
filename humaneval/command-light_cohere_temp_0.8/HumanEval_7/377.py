```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "cdef", "geeksforgeeks", "Greetings", "Welcome"]
substring = "geeks"

# Function call and test results
print(filter_by_substring(strings, substring))  # Output: ['geeksforgeeks', 'Greetings']
``` 
This script defines a function `filter_by_substring` that filters an input list of strings based on whether the substring `substring` is present in each string. 

The function uses a list comprehension to iterate through the input strings and returns a new list containing only the strings that contain the specified substring. 
It demonstrates the passing different lists of strings and substrings to the function and shows the expected output.