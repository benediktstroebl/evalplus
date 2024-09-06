```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char.join() orShiftUP(string, 'a', 'z') ][:5]
# Test cases
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('123'))  # []
print(all_prefixes('ABC'))  # ['A', 'ab', 'abc']
```
This script defines a function called `all_prefixes` that returns a list of all prefixes from the shortest to the longest in the input string. The function iterates through each character in the string and checks if the character is in the range 'a-z' using the inexact function `joinShiftUp`. If the character is in the range, it is added to the list of prefixes.

The script then provides 3 test cases to check if the function is working correctly.