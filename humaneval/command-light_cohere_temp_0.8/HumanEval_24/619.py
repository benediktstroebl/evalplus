```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, max(1, n))
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)
if __name__ == "__main__":
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 4
    assert largest_divisor(24) == 8
    assert largest_divisor(10) == 4
    assert largest_divisor(27) == 9
    assert largest_divisor(49) == 13
``` 
This code defines a function `largest_divisor(n)` that finds the largest divisor of a given number `n`. It uses the `gcd()` function to calculate the greatest common divisor of `n - 1` and the maximum possible divisor less than `n`. 

The `gcd()` function returns the greatest common divisor of 2 numbers. 

This function can be used to find the largest divisor of a number, which is a property used in many algorithms and problems in computer science.