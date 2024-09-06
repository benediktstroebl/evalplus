```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha(string)][]
def isalpha(char):
    return char >= 'a' and char <= 'z'
``` 
This code defines a function called **`all_prefixes`** that returns a list of all prefixes of a given string. It uses a tested to generate a list of all prefixes from the shortest to the longest character in the string. 

The code also includes a helper function, **`isalpha`**, that checks if a character is in the range of lowercase and uppercase letters ('a-z'). 
This function can be used to efficiently filter out non-alphabetic characters from the input string.