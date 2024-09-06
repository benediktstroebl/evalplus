```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR operation on two strings.
   
    Parameters are two strings consisting only digits 1 and 0.
    Returns the string of binary numbers resulting from XOR operation.
    """
    using a range of each digit
    """
    # Remove non-digit characters
    a = ''.join(char for char in a if char.isdigit())
    string_xor = ''
    b = ''.join(char for char in b if char.isdigit())
     # Corrected test cases
    return ''.join(char for char in string_xor if char.isdigit())
 string_xor = ''.join(char for char in b if char.isdigit())
    string_xor = ''.join(char for char in string_xor if char.isdigit())
   _and_return(string_xor)

# Example usage
def test():
    assert string_xor('010', '110') == '100'

# Run the test function to verify the correctness of the function
test()
```