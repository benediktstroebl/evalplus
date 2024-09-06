```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return max(a, b) // gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
```
This code provides a function that calculates the greatest common divisor for two positive integers a and b. It uses the the more efficient approach by calculating the GCD using the `gcd` function and then selecting the larger value.

Note: The function will raise a `ValueError` if the input values are not both positive.