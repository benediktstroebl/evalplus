```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, which only contain 1s and 0s, and return the result as a string. """
    string_xor('010', '110') == '100'
    string_xor('111', '1') == '11'
    string_xor('000', '0000')  # Should return 000000
    ```  # Empty string