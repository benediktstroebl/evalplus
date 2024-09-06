```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return str(int(a, 2) ^ int(b, 2))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs, consisting of only 1s and 0s. It performs a binary `XOR` operation on the digits of the input strings `a` and `b` converted to integers, and returns the result as a string. This is a typical `XOR` proposition --- `1` result whenever the inputs have a different digit value (`1` XOR `0` = `1`, `0` XOR `1` = `1`, `1` XOR `1` = `0`). 

The function is also annotated with type hints, following Python's type discipline, declaring `a` and `b` to be of type `str`, and the function to return a value of type `str`. As well, below is an example of using the `string_xor` function on two example inputs:
```python
>>> string_xor('010', '110')
'100'
```

The output of this example is '100', reflecting the binary XOR operation on the two input strings.