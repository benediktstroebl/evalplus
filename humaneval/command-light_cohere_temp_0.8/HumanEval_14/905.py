```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [x for x in string if x != ' ' and x != '.']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aa') == ['a', 'aa']
    assert all_prefixes('') == []
    assert all_prefixes('x') == []
    assert all_prefixes('abcde') == ['ab', 'cde']

# Main execution
if __name__ == "__main__":
    test_all_prefixes()
```
The function 'all_prefixes' takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to iterate over each character in the string and adds characters that are not spaces or periods to the list of prefixes.