```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # tests
        test
    # just print the function's output
    print(all_prefixes("abc"))
```  This function loops through every character in the string and creates a new prefix by adding each character to the current prefix.