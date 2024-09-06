Here is a Python script that contains a self-contained function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
import string
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    The function uses the string.group method for prefix grouping and the longest prefix generation.

    return [list of prefixes in ascending order of length, starting from the shortest to the longest.
>>> example usage:
>> all_prefixes('abc')
['a', 'ab', 'abc']
"""

    # Preprocessing steps and prefix grouping
    prefixes = string.group(string, False)[0]  # all prefixes and separated by empty string

    # Sorting prefixes by length and returning
    sorted_prefixes = sorted(prefixes, key=lambda x: len(x))
    return sorted_prefixes

```

This function uses the group method to split the input string into a list of prefixes and then sorts the list of prefixes by their length, returning the list of all prefixes in ascending order of length. The example usage provided demonstrates how the run the function and print the expected output.