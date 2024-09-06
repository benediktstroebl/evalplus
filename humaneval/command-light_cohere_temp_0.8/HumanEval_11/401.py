Certainly! Here's a Python script that includes a self-contained function named `string_xor` that solves the given markdown code problem: 
```python
import stringprep as st

def string_xor(a: str, b: str) -> str:
    """
    This function takes two input strings a and b consisting of only characters '0' and '1' and performs binary XOR operation on these inputs and returns the result as a string.
    """
   
    operator over the full implementation of the XOR operation on the two input strings.
    """
   
    below
    operation using the bitwise XOR (^) of the corresponding characters:
    a ^ b
    """
    a = st.char(a)
    b = st.char(b)
    # Concat the result string of the XOR operation
    return "".join(a ^ b)

# Unit tests
test_string_xor = st.test.string("string_xor", '010', '110')
test_xor.test_console = st.test.test_ suite(string_xor, [('string_xor', test_xor)])
``` 

This script includes a function `string_xor` that performs the XOR operation on two input strings. It also passes the value with test cases, which are strings that contain only the characters '0' and '1'.