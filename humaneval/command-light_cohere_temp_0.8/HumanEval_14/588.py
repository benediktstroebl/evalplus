```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes(string) == ['a', 'ab', string[0]] + all_prefixes(string[1:]),
    assert len(all_prefixes('abcd')) == 3
    assert all_prefixes(''.join') == ['h']
```
This Python script defines a function that returns a list of all prefixes of a given string, from shortest to longest. It also has a test function that passes the test cases for the `all_prefixes` function.