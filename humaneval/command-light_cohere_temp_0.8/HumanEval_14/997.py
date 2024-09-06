```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ' ', '!']

# Unit Tests
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("abc123") == ['abc']

if __name__ == "__main__":
    test_all_prefixes()
 ```

This code defines a function all_prefixes that returns a list of prefixes from the input string. It uses a standard list comprehension to filter out all non-space and non-punctuation characters from the string. Then, it returns the specific output for different input cases.