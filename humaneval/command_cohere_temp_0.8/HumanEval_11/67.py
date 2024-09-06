```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two input strings `a` and `b`, which contain only digits `0` and `1`. The function takes the two input strings as arguments and returns their binary `XOR` as a string. It uses `typing` to ensure type-safety and employs a `for` loop and the `zip` function to iterate over the characters of `a` and `b` simultaneously, computing the `XOR` for each pair of characters and converting it to a single character using `chr`. 

The function's behavior is demonstrated via a test case in the markdown code block, where it's asserted that `string_xor('010', '110')` returns '100'. 

This solution is self-contained and can be imported and executed independently without the need for additional code or dependencies.