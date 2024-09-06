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

The function leverages a `for` loop to iterate through each character in the input string. For each character, it appends it to the current prefix, which is initially an empty string. This allows the generation of all possible prefixes from the input string. Subsequently, the function stores these prefixes in the resultant list, enlisting them from the shortest to the longest. 

This approach ensures that each permutation of prefixes is captured, irrespective of the order of characters in the original string. 

If the string is `abc`, the output would be `['a', 'ab', 'abc']`. 

This approach allows the utilization of plain Python, making it widely accessible and efficient in solving the problem.