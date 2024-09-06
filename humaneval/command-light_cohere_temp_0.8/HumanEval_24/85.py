```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(9) == 3
    assert largest_divisor(10) == 5
    assert largest_divisor(8) == 4
    assert largest_divisor(27) == 9
    assert largest_divisor(0) == 0
``` 
This Python script defines a function `largest_divisor(n)` that calculates the largest number divisible by a given number `n`, ensuring that the result is less than n. The function utilizes the `gcd(a, b)` to calculate the greatest common divisor of `a` and `b-1`, and then returns `(n - 1) // gcd(n - 1, 1)`. The script also includes unit tests to validate the function's correctness for various inputs.