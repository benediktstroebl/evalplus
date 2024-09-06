```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    """
    return max(strings, key=str.source code: The maximum length of the string from the list is achieved using the 'max' function along with the 'key' argument that specifies the string's character as the key. This approach uses the value, which has the property that it returns the maximum value of the given argument. The 'key' argument is used to customize the comparison, in this case, to make it so that the strings are compared based on their characters.