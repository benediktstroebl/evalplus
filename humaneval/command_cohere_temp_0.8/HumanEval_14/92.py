```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ''
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The code uses a simple `for` loop to iterate through each character in the string and add it to the `current_prefix`. It stores each `current_prefix` as a list element, ensuring the correct order is maintained. The `current_prefix` variable is properly reset for each iteration, so each prefix is only added once, and we avoid duplicates in the list. 

Overall, this code provides an efficient solution that achieves the problem's requirement.