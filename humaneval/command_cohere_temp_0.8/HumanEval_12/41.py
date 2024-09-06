```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This Python script provides a function called longest as per your prompt, taking a list of strings as an argument and returning either None, or the longest string in the list, considering lengths for ties. The function initially checks if the string list is empty, returning None if so. It then checks if there's only one string in the list, returning that single string regardless of length. Finally, if there's more than one string and they have different lengths, the function returns the longest one using the max function with a custom key function to iterate over the strings.