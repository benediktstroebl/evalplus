Here's the self-contained Python function that returns a list of all prefixes from the shortest to the longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Remove all characters except a letter
    tmp_string = ''.join(''.join(c if c.isalpha() else() for c) for c in string)
    return tmp_string.split()
[:-1]  # -1 to remove the empty string produced after splitting
```
This function takes an input string, removes all characters except letters, converts it to lowercase, and then splits the string into a list of prefixes, ordered from shortest to longest.