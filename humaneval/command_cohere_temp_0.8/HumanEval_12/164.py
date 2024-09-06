```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script provides a function called longest as per your prompt, taking a list of strings as an argument and returning either None, or the longest string if the list contains at least two strings, or the first string if there are multiple strings of the same length.

The function firstly checks if the input list is empty, and returns None if it is. Then it checks if there's only one unique string in the list, and if so, it returns the only string. Lastly, if there's more than one unique string, it uses the max function with a custom key (the length of the string) to confidently return the longest string. 

This solution allows for multiple strings of the same length to be returned as the longest string, following the guideline you provided. I could also rewrite the function to revert to the first string in case of same lengths, should that be preferred. Let me know if you have any questions or feedback on this solution!