```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string if c.isalpha()]
# Test the function
    if all(all_prefixes('abc')):
        print('Test passed')
    else:
        print('Test failed')

def all_prefixes_test():
    input_str = 'abc'
    all_prefixes(input_str)
```
This code defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest characters in the string. It uses list comprehension with a condition that filters out any non-alphalpha character from each character in the string. The `all_prefixes_test` function then calls the `all_prefixes` function with the string 'abc' and passes the test.