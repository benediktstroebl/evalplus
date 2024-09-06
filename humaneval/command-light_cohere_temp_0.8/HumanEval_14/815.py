```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ["".join(c) for c in string if c != '']
``` 
This function takes a string `string` as input and returns a list of all prefixes from shortest to longest of the input string. 
This is done by using list comprehension to filter out all characters that are not spaces from the input string, and then joining them together to get the desired output.