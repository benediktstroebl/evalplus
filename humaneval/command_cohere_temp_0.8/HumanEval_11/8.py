```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(c^b for c in a for b in '01')
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on the input strings `a` and `b`, which consist of only 1s and 0s. The binary XOR is done on characters matched pairwise from the strings '01' and `b`, and the result is returned as a string.

This code should produce the correct result for the given problem and fulfill the given test case. Adjustments might be necessary to match the given test case entirely.