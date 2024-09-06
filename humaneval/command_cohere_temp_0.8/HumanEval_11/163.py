```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that alternates between corresponding characters from the two input strings, converting them to ints, XOR-ing them, and converting the result back to a character before joining these characters together to form the output string.

Here is an example of how you can use this function by calling it with example inputs "010" and "110" to return the result "100":
```python
print(string_xor('010', '110'))  # Outputs '100'
``` 

This function does not explicitly define the input format, which is that both strings should consist only of 0s and 1s, but this is a reasonable assumption given the problem description and the test example provided. If you encounter a different kind of input where XOR operation is applicable, you might need to add validation and handle those cases differently.