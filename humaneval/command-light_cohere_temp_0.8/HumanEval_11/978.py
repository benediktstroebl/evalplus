```python
import stringIO
from typing import List
def string_xor(a: List[str], b: List[str]) -> List[str]:
    """ Inputs are two lists of strings, a and b consisting only of ASCII characters.
    Perform binary XOR on each inputs and return result also as a list of strings.
    """
   
    list comprehension is essential for this problem.
    """return [[[c ^ d for c, d in zip(a, b)])
    """
    return [c for c in ''.joinjoin([c ^ d for d in b])
def test_string_xor():
    s = ['010', '110', '1001', '0011', '1010', '1010']
    t = ['100', '10', '1000', '001', '110', '1010']
    assert string_xor(s, t) == ['100', '101', '1001', '01', '1011', '101010']

# Reading the test file and executing the test function
with stringIO.read('tests.txt') as f:
    for _ in f:
        test_string_xor()

```
This script defines a function `string_xor` that performs a XOR operation on two input strings, which are lists of ASCII characters. It then defines a test function that reads a test file, iterates over the test cases, and passes each test by comparing the output of `string_xor` with the expected output.