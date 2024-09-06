```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, max(1, int))
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
def test1():
    assert largest_divisor(15) == 5
def test2():
    assert largest_divisor(1) == 1
def test3():
    assert largest_divisor(7) == 1
def test4():
    assert largest_divisor(19) == 5
``` 
This Python code defines a function `largest_divisor(n)` that returns the largest integer that evenly divides `n`, ensuring that the result is less than or equal to `n`. It also defines a function `gcd(x, y)` that calculates the greatest common divisor of two integers `x` and `y`. The `test1()` function verifies that the `largest_divisor` function correctly returns 5 when passed 15, the `test2()` function checks that it returns 1 for 1, the `test3()` function checks that it returns 1 for 7, and the `test4()` function checks that it returns 5 for 19.  This framework efficiently organizes code for a problem and provides a clear and concise way to test its functionality.