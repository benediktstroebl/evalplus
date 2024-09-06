```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(prefix) for prefix in re.io.split(string)[0::2:-1]]

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("abc\defg") == ['abc', 'defg']

if __name__ == "__main__":
    test_all_prefixes()
 ``` 
This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest in the input string. It utilizes the `re.split` to split the's the input string into prefixes and then selects the prefixes from the start to the second-last character of the string.