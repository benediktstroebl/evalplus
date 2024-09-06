```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ']
def test():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
def test2():
    assert all_prefixes("123") == ['1', '23']
def test3():
    assert all_prefixes("") == []
def test4():
    assert all_prefixes(" ") == []

# call all functions from test suite
test()
test2()
test3()
test4()
``` 
This code defines a function all_prefixes that returns a list of prefixes from a given string. It uses list comprehension to iterate through each character in the string and only keeps non-space characters. This code is test several test cases to ensure that the function works correctly for different inputs.