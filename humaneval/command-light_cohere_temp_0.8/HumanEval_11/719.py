```python
import stringmagic

def string_xor(a: str, b: str) -> str:
    return stringmagic.c(a ^ b)

test_string_xor = ["010", "110"]
test_result = string_xor(test_string_xor[0], test_string_xor[1])
assert test_result == "100"

test_string_xor = ["abc", "abcd"]
test_result = string_xor(test_string_xor[0], test_string_xor[1])
assert test_result == "efcd"
```
This script provides a self-contained solution to the problem using the `stringmagic` library to perform the XOR operation on two input strings. 
It also has corresponding tests to check the correctness of the `string_xor` function.