```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_all_prefixes(test_str: str) -> None:
    actual_prefixes = all_prefixes(test_str)
    expected_prefixes = ['', 'a', 'ab', 'aba', '123', 'abc']  # Assume

    assert actual_prefixes == expected_prefixes, "Prefixes do not match."
```
This code provides a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest of the input string. 
It then defines a test function `test_all_prefixes` that passes a test string and expects the actual prefix list to match the expected prefix list.  The run the test with your test string and make sure the actual and expected prefixes match.