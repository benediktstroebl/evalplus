```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string]

# Test the function
test_string = "abc"
result = all_prefixes(test_string)
print(result)  # Output: ['a', 'ab', 'abc']
``` 
This code defines a Python function `all_prefixes`, which returns a list of all prefixes of a given string.  It uses a string as an parameter, and iterates through each character in the string, creating each prefix with the preceding characters removed.