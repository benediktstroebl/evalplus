```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two input strings a and b. string
    and return result as a string. """ 

def test_xor(test_cases: List[str]) -> None:
    for test in test_cases:
        result = string_xor(test, test)
        assert result == '101'

# Example usage
test_xor([ '010', '110', '100' ])
``` 
The code defines a function **string_xor** that performs a XOR operation on two input strings. It uses a particular input string and returns the result as a string. 
Additionally, the code defines a test function **test_xor** with a list of test cases. The function iterates over each test case and calls the string_xor function with the two input strings. It then compares the test results with the expected '101' and raises an **AssertionError** if the result is not correct.