```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.split() if len(string) > 1]

# Test case
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
The function `all_prefixes` uses the Python split method with a length greater than 1 to get all prefixes from the shortest to the longest word in the input string.