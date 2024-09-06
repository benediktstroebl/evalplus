```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script provides a function called longest as per your prompt, taking a list of strings as an argument and returning either None, or the longest string in the list, handling the tiecase scenario by returning the first longest string encountered. 

The function utilises the len function to determine the longest string by utilising the max function and identifying the key parameter as string length.