```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.br.split()]

    def test_all_prefixes() -> None:
    input_str = "abc"
    expected = ['a', 'ab', 'abc']
    actual = all_prefixes(input_str)
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

# Call the function and test it
test_all_prefixes()
 ```
This script defines a function `all_prefixes` that returns a list of all prefixes in a given string. It also includes a test function with an assert statement that verifies if the function's output matches the expected output.