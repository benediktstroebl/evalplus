```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two input strings composed of only digits 1 and 0 and return the result as a string. """
    Low level code for this string operations are very efficient and common. """
    a function could also use the types to help with potential type issues and have built-in error checking around them. 
Expected input:
    - Two strings consisting only of digits 1 and 0.
Expected Output:
    - The result of XOR operation between the two input strings
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Input must be strings")

    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")

    result = []
    for c in a + b:
        if c == "0":
            result.append(0)
        elif c == "1":
            result.append(1)
    else:
            result.append(c)

    return "".join(result)
```

The provided Python script defines a function `string_xor` that performs the XOR operation on two input strings containing only digits 1 and 0. The function ensures that the input is of type string and has the same length. It uses a list comprehension to build the result string, checking each character in the input strings and append the corresponding character to the result string.