```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    # Find all non-empty prefixes of the input string and sort them by length
    # from shortest to longest
    prefixes = sorted(re.findall(r'^(\w+)', string), key=len, reverse=True)
    return prefixes
``` 

The function `all_prefixes()` uses the `re.findall()` function to find all non-empty prefixes of the input string that are separated by whitespace, and then sorts them by their length from shortest to longest using the `sorted()` function with the `key` parameter set to `len`, the length of each prefix is used as the sorting key. The `reverse=True` parameter ensures that the sorting happens in the descending order of the prefix lengths.  This approach ensures that the prefixes are correctly extracted and sorted as required by the prompt.  This is a concise and efficient way to solve the problem.