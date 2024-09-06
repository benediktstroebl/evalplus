```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i else '']

# Test the function
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aa') == ['a', 'aa']
    assert all_prefixes('abcde') == ['abcde']

if __name__ == '__main__':
    test()
```
This code defines a function called all_prefixes, which takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension with a generator expression to iterate over each character in the string, and includes the empty string at the end.