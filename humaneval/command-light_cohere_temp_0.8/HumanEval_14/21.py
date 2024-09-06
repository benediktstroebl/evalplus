Here is a Python script that contains a self-contained function that generates all prefixes from the shortest to the longest of any input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join([char for char in s]) for s in string.
# Test cases
print(all_prefixes('abc')) # ['a', 'ab', 'bc']
print(all_prefixes(''abc')) # ['a', 'ab', 'abc']
```
This script defines a function called all_prefixes that takes a string as input and returns a list of all prefixes. The test cases section verifies that the output is correct for different inputs.