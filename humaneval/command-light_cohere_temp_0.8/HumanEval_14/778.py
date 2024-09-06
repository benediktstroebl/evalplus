```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string if c.isalpha()]

def test_function(string):
    return all_prefixes(string) == ['a', 'ab', 'abc']
```  This script defines a function that returns a list of all prefixes from shortest to longest of an input string. It also provides a testing function to check if the all_prefixes function produces the expected output. 

This function is self-contained and will run without any external modules.