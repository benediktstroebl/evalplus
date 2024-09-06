```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list.
    """
    list of strings to be passed as an argument.
    # we use the Mapp and str methods to convert the list of strings to a list of characters.
    str = ''.join(strings)
    # we use the max function to find the length of the longest string
    return max(str)
```
The provided solution uses the Python 'max' function in combination with the 'max' built-in function, along with 'str.sleep' to identify the string characters and determine the length of the longest string in the list. 

We then pass the test by providing an empty list and an input list with the same length containing different strings.