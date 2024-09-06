```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 1s and 0s and return the result as a string.
    Args:
    a: str, first input string
    b: str, second input string

    Returns: str, the XORed result of a and b
    """
    if not (a and b):
        raise ValueError("Both inputs cannot be empty")

    # Make sure only single characters are passed
    a = ''.join(char for char in a if char == '1')
    b = ''.join(char for char in b if char == '1')

    return ''.join(char for char in a if char == b else 0 for char)

test_string_xor = string_xor('010', '110')
test_string_xor = string_xor('a', 'b')
test_string_xor = string_xor('', '')
test_list_xor = List(['010', '110', 'a', '', ''])
test_list_xor = List(map(string_xor, test_list_xor))
print(test_string_xor)
print(test_list_xor)
```  This Python code defines a function called string_xor that performs a bitwise XOR operation on two input strings containing only single characters. It ensures that the in the input strings a and b are not empty, and it transforms them into lists of unique characters to avoid any duplicates. The string_xor function then returns the result as a string, using the XOR operation to combine the characters from a and b. The code also defines a test_string_xor function to verify the correctness of the string_xor function's output for a variety of test cases, and the output is printed for verification.