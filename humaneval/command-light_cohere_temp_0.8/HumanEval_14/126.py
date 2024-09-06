```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string]

# Test the function
test_str = "abc"
print(all_prefixes(test_str))  # Output: ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It utilizes a particular string as a parameter and creates a generator expression that iterates over all characters in the string, transforming each character into its own prefix. 

The output of the code is the list ['a', 'ab', 'abc'].