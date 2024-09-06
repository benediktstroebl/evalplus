```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the longest string from the list"""
    return max(strings, key=len)

# Example usage
strings = ["a", "b", "c"]
print(longest(strings))  # Output: "c"

strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: "ccc"

strings = []
strings. strings longest(["a", "aa", "aaaa"]) # Output: "aaaa"
``` 
This code provides a solution to the problem, which is to find the longest string in a list of strings. It does so by using the max function with the key=len function, which returns the length of the string. This is the longest string from the list.