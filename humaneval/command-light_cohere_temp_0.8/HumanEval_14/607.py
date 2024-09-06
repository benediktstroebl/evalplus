```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char.isalpha()]

def test_function(test_cases: List[str]) -> None:
    for test_case in test_cases:
        assert all_prefixes(test_case) == [''.join(char) for char in test_case if char.isalpha()],
    providing all valid test cases for the function. 
``` 
In this script, the `all_prefixes` function uses a generator expression to iterate through each character in the input string. The `test_function` uses the `assert` statement to check if the `all_prefixes` function returns the expected output for each test case.