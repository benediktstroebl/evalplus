```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", " greeting"]
substring = "a"

# Function call and expected output
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
The Python code defines a function `filter_by_substring` that filters a list of strings based on containing a given substring. The function uses a list comprehension to iterate over the input strings and checks if each string contains the specified substring. The result is then stored in a new list, which can be easily printed or used in other parts of the code.