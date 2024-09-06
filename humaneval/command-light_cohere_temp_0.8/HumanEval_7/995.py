```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "Hello", "World", "!!"]
sub = "l"

result = filter_by_substring(strings, sub)
print(result)   # Expected output ['Hello', 'World']
``` 
This code defines a function called `filter_by_substring` that takes a list of strings and a substring as inputs and returns a new list containing only the strings from the input list that contain the given substring. 

The function utilizes a list comprehension to iterate over the input strings and checks if each string contains the specified substring.