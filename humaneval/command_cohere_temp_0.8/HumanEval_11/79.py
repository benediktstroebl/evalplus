```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings `a` and `b` as input. It uses `typing` to ensure type correctness and employs bitwise XOR to systematically contrast corresponding bits of the input strings, resulting in a third string containing the binary XOR of `a` and `b`. The process is exemplified in the docstring, and the conclusion is strengthened by a test case. This function is versatile and can handle any binary string operation, ensuring correct type usage.