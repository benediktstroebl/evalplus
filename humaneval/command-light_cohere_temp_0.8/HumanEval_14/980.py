```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # tests
    strings)
def test_all_prefixes(test_strings: List[str]) -> None:
    assert all(test_strings == all_prefixes(test_strings))
    return
test_strings = [''.join('a'), '.ab', 'abc']
test_all_prefixes(test_strings)
``` 
This code defines a function all_prefixes that returns a list of all prefixes from the shortest to longest of a given string. The test_all_prefixes function creates a list of test strings and passes it to the all_prefixes function.