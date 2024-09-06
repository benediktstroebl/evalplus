```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of digits 1-9.
    result = []
    for char in a+b:
        if char=='0':
            result.append('0')
       
        elif char=='1':
            result.append('1')
       
    else:
            result.append(char)
    result = ''.join(result)
    return result

# Test cases and their expected results:
test_cases = [
    ("010", "110"),
    ("1010", "001"),
    ("000", "100"),
    ("1111", "11"),
    ("00", "")
]

for case, expected in test_cases:
    actual = string_xor(*case.strip())
    print(f'Case: {case}')
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
```  The output will display the input string with the corresponding expected result.  This for each function, it uses a loop to perform a XOR operation on the two input strings. The function then returns the string of the resulting characters.