```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != ' ', ]

# Test case 1
test_case1 = "abc"
print(all_prefixes(test_case1))  # Expected Output: ['a', 'ab', 'abc']

# Test case 2
test_case2 = "xvillagey"
print(all_prefixes(test_case2))  # Expected Output: []

# Test case 3
test_case3 = "hello, hello!"
print(all_prefixes(test_case3))  # Expected Output: ['h', 'hello']
```
This script defines a function all_prefixes that returns a list of all prefixes in a given string. The function uses list comprehension to iterate over each character in the string, and only keeps characters that are not spaces. 
The test cases demonstrate the function's behavior for different inputs.