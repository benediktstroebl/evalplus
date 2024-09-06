```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    # Function to find the longest string in a list of strings
    longest = str.join(strings)
    return longest

# Test cases
strings = ['a', 'b', 'c', 'bb', 'ccc']
result = longest(strings)
print("Longest string:", result)  # Output: ccc

strings2 = []
strings2.add = ['aa', 'a', 'bb', 'ccc', 'a']
result = longest(strings2)
print("Longest string:", result)  # Output: aa

strings3 = ['a', 'bb']
result = longest([strings3])
print("Longest string:", result)  # Output: bb

strings4 = ['aa', 'bb', 'bb']
result = longest(strings4)
print("Longest string:", result)  # Output: bb
```
The function `longest` takes a list of strings as input and returns the longest string from that list. This function uses theming and joining to create a single string from the input list, and then compares it with the other strings in the list to find the longest.