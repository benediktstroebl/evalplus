```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
strings. strings longest(strings)
print(f'Longest string is "{longest}" with length {len(longest)}')

strings = []
strings = [None]
strings = ['a', 'bb', 'ccc']
strings = ['a'] + ['bc'] + ['cd']
longest(strings)
print(f'Longest string is {longest} with length {len(longest)}')

# Example case with empty input list
strings = []
print(longest(strings)))
```
This code defines a function called `longest` that takes a list of strings and returns the longest string from that list. It uses the max function along with the key argument set to `len`, so that the longest string is always returned. The function is tested using several test cases, and the output is displayed.