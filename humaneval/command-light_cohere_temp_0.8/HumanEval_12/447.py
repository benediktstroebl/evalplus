```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    # function to get the length of a string
    def length(string): return len(string)
    
    # function to compare two strings length
    def length_compare(string1, string2): 
        return length(string1) > length(string2)
        
    # function to find the longest string in list
    return max(strings, key=length_compare)

# test cases
print(longest(['a', 'b', 'c']))     # Output: 'c'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))          # Output: ' ' or None
``` 
This code introduces a self-contained solution for the given problem. It utilizes a two functions: length() to calculate the length of a given string, and length_compare() to compare the lengths of two strings and return a boolean result. The last function, max(), takes a list of strings and a key function (which is our custom length_compare() function), and returns the element in the list that the key function returns True for.

This code is self-contained and does not require any external modules or functions. It can easily be imported and called as a function in another script.