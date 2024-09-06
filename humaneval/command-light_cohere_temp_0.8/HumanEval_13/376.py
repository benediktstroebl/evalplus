```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required.")
    while a != 1 or b != 1:
        if a & b == 0:
            break
        a, b = divmod(a, b)
    return min(a, b)

# Unit tests
test_gcd = lambda: assert greatest_common_divisor(3, 5) == 1
test_gcd()
test_gcd(25, 15)
test_gcd(10, 5)
test_gcd(2, 25)
test_gcd(4, 20)
test_gcd(6, 60)
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers. The function uses the method 'divmod' to calculate the greatest common divisor by repeatedly dividing the larger number by the smaller number until the result is non-zero, then taking the minimum of the two numbers. 

The code also includes unit tests using the `assert` statement to verify the correctness of the `greatest_common_divisor` function.