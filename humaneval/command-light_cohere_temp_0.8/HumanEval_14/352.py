```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(*i) for i in zip(*(string[::i] for i in range(1, len(string) + 1) if i <= len(string)))]
# Tests
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('') == []
assert all_prefixes('abcde') == ['abcd', 'abcde']
assert all_prefixes('a') == ['a']
assert all_prefixes(''). == []
assert all_prefixes('xxyx') == ['xyx']
```  This code provides a function all_prefixes that accepts a string s as input and returns a list of all prefixes from shortest to longest. This is achieved by using the `zip()` and the `range()` function to iterate over all possible prefixes of the string, selecting only the prefixes of length 1 to n.