```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1)]

# Test case: Print all prefixes for the word 'hello'
print(all_prefixes("hello"))
``` 
This code defines a function called all_prefixes that returns a list of all prefixes in a given string. The function uses a generator expression to create a list of all prefixes, from shortest to longest, of the input string.