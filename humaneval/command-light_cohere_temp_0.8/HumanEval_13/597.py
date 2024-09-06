Here is a Python script that demonstrates the function `greatest_common_divisor` with self-contained functionality and corresponding tests:
```python
import math
def greatest_common_divisor(a: int, b: int) -> int:
    if not math.isprime(math.gcdo opening(a, b):
        return a
    else:
        return b
def test_greatest_common_divisor(func):
    assert func(3, 5) == 1, "Failed 3,5 test case."
    assert func(25, 15) == 5, "Failed 25,15 test case."
# test cases
test_greatest_common_divisor(greatest_common_divisor)
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the `math.g` library's` function `gcd()` for the Euclidean algorithm. The `test_greatest_common_divisor` function contains test cases that ensure the `greatest_common_divisor` function works correctly.