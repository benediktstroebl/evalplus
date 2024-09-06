```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '{0}{1}'.format(*[int(x) ^ int(y) for x, y in zip(a, b) if x == '1' or y == '1'])
```

This approach performs the binary `XOR` operation on the two strings (`a` and `b`) and returns the result as a string. Here's an explanation of the steps:
1. The function `string_xor` takes two string inputs (`a` and `b`) of binary strings consisting of only `0`s and `1`s.
2. We use `zip` to iterate over the corresponding bits of the two strings, taking pairs of bits (one from each string) and casting them to integers.
3. We use bitwise `XOR (`^`) on each corresponding pair of integers, ensuring that only bits with a value of `1` in either string will be XORed, as specified in the problem.
4. We use `format` to reconstruct a string from the binary values returned from the `^`, which will be `0` and `1`.

The format method is used to concatonate the two strings together, with the `{}` yielding the correct placeholders and `0` and `1` being replaced with the results of the bitwise operation.

This function effectively performs binary `XOR` on the two input strings and returns the result as a string, as required by the problem statement.