```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1) if string[i] == string[i - 1]]
def test_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
This code defines a function that returns a list of all prefixes from shortest to longest of an input string. It uses a also uses a List comprehension to achieve this. Additionally test_ prefixes function is then tested with the 'abc' string and the test_prefixes function asserts the result of the function.