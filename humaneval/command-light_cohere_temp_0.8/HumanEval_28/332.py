```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(s) + ''.join(strings)
if __name__ == "__main__":
    test_strings = [''] + ['a', 'b', 'c']
    result = concatenate(test_strings)
    assert result == 'abc'
```