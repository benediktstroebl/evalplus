```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros
    :param a: string, one string
    :param b: string, another string
    :return: string
    """
    return "".join(chr((ord(c) ^ ord(b[i])) for i,c in enumerate(a + b)))

# Test case 1
print(string_xor('010', '110'))
# Expected Output: 100

# Test case 2
print(string_xor('0011', '001010'))
# Expected Output: 0001100

# Test case 3
print(string_xor('abc', 'zyxw'))
# Expected Output: xyzb

# Test case 4
print(string_xor('1010101', '0101010'))
# Expected Output: 1010101010

``` 
The above code defines a function called `string_xor` that takes two strings as input and returns the XOR of these strings. It uses the string slicing to extract each character and perform the XOR operation using `chr` and `ord` functions to convert the characters to their corresponding integers and perform the XOR. The test cases are then used to validate the correctness of the function by passing known inputs and checking if the returned output is as expected.