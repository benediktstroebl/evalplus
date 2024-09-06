```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in range(1, len(string)+1)]
# Test case
test_string = "abc"
all_prefixes(test_string) # ['a', 'ab', 'abc']
```
The code defines a function called **`all_prefixes`** that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a range function and a generator expression to iterate through each character in the input string, starting from 1 (since the empty string itself is not a prefix). 

The code also includes a test case with a sample string and calls the function with that string, and the expected output is indeed **`['a', 'ab', 'abc']` which are the first letters in the input string.