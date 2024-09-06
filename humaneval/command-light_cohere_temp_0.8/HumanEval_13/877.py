Here's the improved Python script with self-contained function:
```python
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

def test_gcd():
    assert gcd(3, 5) == 1
    assert gcd(25, 15) == 5
```
The above code defines a function `gcd` that calculates the greatest common divisor of two integers using the Euclidean algorithm. It also has tests the simple and efficient implementation of the `gcd` function. The `test_gcd` function contains some assertions to test the `gcd` function with various inputs and ensures the correctness of the function.