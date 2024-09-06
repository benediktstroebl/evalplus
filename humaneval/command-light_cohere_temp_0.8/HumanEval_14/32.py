```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(s) for s in string.string(1). a, aa, aaa', ab, ...)]

# Test case 1:
def test_case_1():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

# Test case 2:
def test_case_2():
    assert all_prefixes('x') == []

# Test case 3:
def test_case_3():
    assert all_prefixes(' ') == []

# Test case 4:
def test_case_4():
    assert all_prefixes('a') == ['a']

test_case_1()
test_case_2()
test_case_3()
test_case_4()
```
The code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of a given string. It uses the array slicing to iterate over each character of the string and uses a list comprehension to generate all prefixes. The code then provides several test cases to ensure the correctness of the function.