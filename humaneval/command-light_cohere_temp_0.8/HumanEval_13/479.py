```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers using the `gcd` helper function. The `gcd` function calculates the maximum of two numbers and their greatest common divisor using the Euclidean Algorithm for the greatest common divisor calculation. 

This function provides a straightforward and efficient way to find the greatest common divisor of two numbers.