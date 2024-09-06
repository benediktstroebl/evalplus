```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring.

    :string comparison is done using the `isublen()` to ensure substring length.

    return: all strings that contain the given substring as a prefix.
    """
Return: filtered list of strings
    """
    return [string for string in strings if len(substring) == len(string)]

# Example usage
my_list = ['abc', 'bacd', 'cde', 'array', 'abcd']
print(filter_by_substring(my_list, 'a'))
 ```