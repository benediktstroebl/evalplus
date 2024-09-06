```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i != '' and i != '']
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
def test1():
    assert all_prefixes('') == []
def test2():
    assert all_prefixes('  ') == []
def test3():
    assert all_prefixes('xyd') == ['x']
def test4():
    assert all_prefixes('xy') == ['y']
test()  # Call function with test() decorator
```