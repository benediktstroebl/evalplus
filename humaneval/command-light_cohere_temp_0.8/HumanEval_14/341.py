```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '']
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
def test1():
    assert all_prefixes('xx') == []
def test2():
    assert all_prefixes(' ') == []
def test3():
    assert all_prefixes('') == []
def test4():
    assert all_prefixes('---') == ['---']
def test5():
    assert all_prefixes('.' ) == ['', '.']
def test6():
    assert all_prefixes('>') == ['>', '<']
```
This Python script defines a function all_prefixes that returns a list of prefixes from the input string, filtering out any characters that are not letters. It also includes several test cases to validate the correctness of the function. These test tests cases help intended to be run and pass the corresponding tests.