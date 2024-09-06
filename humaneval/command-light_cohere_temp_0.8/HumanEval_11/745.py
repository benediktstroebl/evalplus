Certainly! Here is a self-contained Python function that performs the XOR operation on two strings consisting of only digits: 
```python
import string

def string_xor(a: str, b: str) -> str:
    return ''.join(chr((ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test case: "010" XOR "110"
test_cases = [string_xor('010', '110'),
         string_xor('001', '100'),
         string_xor('1010', '0110'),
         string_xor('000', '1111')]

# Loop through each test case and assert the result is correct
for test_case in test_cases:
  assert test_case == '100'

```
This script defines a function `string_xor` that takes two strings `a` and `b` as arguments, performs the XOR operation on the characters in these strings, and returns the result as a string. It also includes a test cases to verify the functionality of the `string_xor` function. 

Let's take a look together: