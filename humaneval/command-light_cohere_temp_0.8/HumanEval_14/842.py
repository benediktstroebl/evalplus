```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ''] + string.test = [assert_list('abc'.split()) == all_prefixes('abc')
```
This code defines a function called `all_prefixes` that takes a string as input and returns a list of all prefixes in the string, starting from the shortest to the longest. The function uses a list comprehension with a lambda function to create the list of prefixes. The test suite is used to verify the correctness of the `all_prefixes` function by checking if it produces the expected output for the test input.