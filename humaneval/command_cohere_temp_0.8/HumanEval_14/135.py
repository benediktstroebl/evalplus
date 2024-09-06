```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ""
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The code uses a simple `for` loop to iterate through each character in the string and adds it to the `current_prefix`. It keeps track of the prefixes in the `prefixes` list, which it then returns. The loop starts with an empty string for the `current_prefix` and builds up from there, ensuring that the prefixes are stored in ascending order.