```python
import stringio
from typing import List
def string_xor(a: List[str], b: List[str]) -> List[str]:
    """ Perform XOR operation on the list of strings.
    """
    expected return is list of the XOR of input strings.
    """
    expected input: two lists of strings consisting only of characters 1 and 0
    """
    out = []
    for i in range(len(a)):
        out.append((a ^ b[i] ^ a[i])
    return out
# Example usage
input_strings = ["010","110","100"]
expected_output = ["100","101","0"]
result = string_xor(input_strings, input_strings)
print("Expected output:", expected_output)
print("Result:", result)
```