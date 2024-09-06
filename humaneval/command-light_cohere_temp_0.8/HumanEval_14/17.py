```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c.isalpha()]

def test_function():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
test_function()
```
The above code defines a function all_prefixes that returns a list of prefixes from the shortest to the longest occurring characters in the input string. It uses a generated using the string's character attributes (isalpha) to filter out non-alph characters.