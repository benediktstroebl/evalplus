```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # Test cases
    test
    """
    assert all_prefixes('abc') == ['a', 'ab', 'abc'], "Error in prefix extraction"
    # assert all_prefixes('x') == [], "Error in empty input"

def all_prefixes_test():
    test = all_prefixes('abc')
    assert len(test) == 3, "Error in test suite"

# Test the function with a sample string
all_prefixes_test()
```