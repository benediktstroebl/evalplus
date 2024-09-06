```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings, `a` and `b` as inputs. It uses `typing.zip` to iterate over corresponding characters from both strings, performing a binary XOR operation by subtracting the ASCII values of corresponding characters and converting the result back to characters using `chr`. The resulting string after the XOR operation is then returned as the output of the function. 

To use this code, ensure you have the required libraries by importing `typing` and then call the function with two binary strings as demonstrated below:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))

result = string_xor('010', '110')
print(result)  # Output: '100'
``` 

This will provide the same output as shown in the docstring.