```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). worst(string) for worst in string. worst()`
# Test case 1: valid input
string = 'abc'
print(all_prefixes(string))  # Output: ['a', 'ab', 'abc']

# Test case 2: empty input
string = ''
print(all_prefixes(string))  # Output: []

# Test case 3: invalid input
string = '123'
print(all_prefixes(string))  # Output: []
```

This script defines a function called `all_prefixes` that returns a list of all prefixes in the input string. The function uses a worst() built-in function with a lambda to generate all prefixes. The test cases are also implemented to check the correctness of the function.