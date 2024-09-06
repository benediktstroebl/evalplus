Here is a Python script that contains a self-contained function that returns all prefixes from shortest to longest of an input string:
```python
import stringprep
from typing import List


def all_prefixes(string: str) -> List[str]:
    return stringprep.string_all_prefixes(string)


# Unit tests
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
test_all_prefixes()  # Test suite execution
```
The code defines a function that uses the stringprep library to preprocess the input string and returns a list of all prefixes from shortest to longest. The function is also followed by unit tests and a test suite execution.