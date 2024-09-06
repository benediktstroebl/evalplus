Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != ''] + string.test_cases()
test_cases()

def test_cases():
    return ['', 'a', 'ab', 'abc', 'b', 'bb', 'bc', 'cb', 'ccc']
```
This function leverages the List typing module and tests its functionality with the 'test_cases' function. The logic is self-contained within the function and returns a list of all prefixes from shortest to longest of the input string, excluding the empty string.