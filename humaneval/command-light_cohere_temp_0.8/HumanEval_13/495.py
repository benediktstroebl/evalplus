```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    # check for both numbers being odd or even
    if a & 1 == 0 and b & 1 == 0:
        return max(divisor(a, b), divisor(b, a))
    else:
        # Calculate the greatest common divisor using the Extended Euclidean Algorithm
        gcd = divisor(a, b)
        t = b // gcd
        b %= gcd
        a %= gcd
        return gcd

def divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    else:
        return b
```
The above Python script defines a function called `greatest_common_divisor` that computes the greatest common divisor of two numbers a and b using the Extended Euclidean Algorithm. The script also includes a helper function `divisor` which checks for zero and returns 0, and calculates the GCD of two numbers using the Extended Euclidean Algorithm.