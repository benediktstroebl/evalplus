Here's a self-contained Python script that provides a function that takes a string as input and returns a list of its prefixes from shortest to longest:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix]
```

# Tests
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This script includes the all_prefixes function that uses a generator expression to extract all prefixes from the input string, and the test_all_prefixes function to verify the correctness of the function's output. 
Feel free to use this script for your problem and test your code accordingly!