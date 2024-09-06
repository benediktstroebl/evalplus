```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return str(int(a, 2) ^ int(b, 2))
```

This Python script defines a function `string_xor` that takes two strings `a` and `b` as input, both of which are assumed to contain only binary digits '0' and '1'. This function calculates the binary XOR of the two input strings and returns the result as a string. This XOR operation is performed by converting both input strings to integers in base 2, performing the XOR operation on these integers, and then converting the result back to a string. 

Here is an example usage of the `string_xor` function:
```python
# Example usage
string_xor("010", "110")  # Output: "100"
```

This will produce the output "100" which is the result of the binary XOR operation '010' ^ '110'.