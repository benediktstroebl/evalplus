```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two input strings.
    :paramstring_xor str1: str, str -> str
    :return string_xor
    """
    # Remove all non-alphphanumeric characters from the input strings
    a = ''.join(char for char in a if char.isalpha())
    string_xor = b = ''.join(char for char in b if char.isalpha())

    string_xor = a ^ b
    return string_xor

# Test cases
test_cases = [
    ("010", "110"),
    ("abc", "123"),
    (" ", ""),
    ("a", "b"),
    ("111", "11"),
]

for t in test_cases:
    result = string_xor(*t)
    print(f"Input: {t[0]} {t[1]}, Result: {result}")
``` 

The above code defines a function `string_xor` that takes two strings and performs XOR operation on them, then returns the result. The type hint is used to specify the expected return type of the function. It also includes test cases to check the functionality of the function.