```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char != ' ' and i != 0]
def test():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
The provided code defines a function called **`all_prefixes`** that returns a list of all prefixes from the shortest to the longest of the input string. It uses a test list comprehension to iterate through each character of the string, except spaces, and includes the character in the resulting list. 
The test function asserts that the output of the **`all_prefixes`** function is correct for the input string "abc".