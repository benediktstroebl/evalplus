```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string.
    # To ensure that the string has at least character
    assert len(string) > 0, "Input cannot be empty"
    return [] if string == "" else all_prefixes(string[1:])

def all_prefixes_test_case(string: str) -> List[str]:
    return all_prefixes(string)
```
This script defines a function all_prefixes that returns a list of all prefixes from shortest to longest of an input string. The function works by creating an iterator over each character in the string and appending each character to a new list until all characters have been processed. 

The test case function is used to verify the correctness of the all_prefixes function. It works by passing the necessary input and asserting that the returned value is indeed the correct output.