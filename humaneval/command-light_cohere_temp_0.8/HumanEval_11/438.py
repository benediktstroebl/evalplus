```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only digits
    """
    # test case 1
    assert stringio.read(string_xor('010', '110')).decode() == '100'

    # test case 2
    assert stringio.read(string_xor('00001', '11')).decode() == '01'

    # test case 3
    assert stringio.read(string_xor('000', '1')).decode() == '1'

    # test case 4
    assert stringio.read(string_xor('000', '9')).decode() == '99'

    # test case 5
    assert stringio.read(string_xor('01', '001')).decode() == '100'

    return 'Result'  # Corrected return statement
```