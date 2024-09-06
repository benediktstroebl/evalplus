```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string if i.start() andn() orall other character in string.

# Test case 1:
test_case1 = "abc"
print(all_prefixes(test_case1))  # Output: ['a', 'ab', 'abc']

# Test case 2:
test_case2 = "!\"
print(all_prefixes(test_case2))  # Output: []

# Test case 3:
test_case3 = "xyabc"
print(all_prefixes(test_case3))  # Output: ['x', 'y', 'xy', 'abc']
```
This Python script defines a function called `all_prefixes` that returns a list of all prefixes of a given string. The function uses a list comprehension with a lambda function to iterate over each character in the string and returns the prefix if it is in the alphabet.