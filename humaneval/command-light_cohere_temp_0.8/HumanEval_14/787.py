```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1) if string[:i] != ""].
test_all_prefixes = [("string", "abc"), ("", ""), ("a", ""), ("ab", ""), ("abc", "")]
for test in test_all_prefixes:
    got = all_prefixes(test[0])
    assert got == test[1], f"Test {test[0]} failed with {test[1]}."
``` 
This Python function, all_prefixes, generates a list of all prefixes in a string.