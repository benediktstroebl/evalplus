```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

#Test the function
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
```
The code defines a function called `longest` that takes a list of strings as input and returns the longest string among them. It uses the process to identify the longest string by finding the string with the maximum length, according to the `len` function. The test case demonstrates the use of the function, passing a list of strings and printing the result.