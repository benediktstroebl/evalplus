```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Test cases
def test_all_prefixes():
    assert all_prefixes("hello") == ['h', 'el', 'll']
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("   ") == []  # Empty string
    assert all_prefixes("\t det\t") == ['\t', 'd', '\t']
    assert all_prefixes("123") == ['1', '23']

if __name__ == "__main__":
    test_all_prefixes()
```
This Python script defines a function all_prefixes that returns a list of prefixes from the input string. It uses a particular set of characters to filter out any whitespace characters from the string.