```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(16), 8)
assertEqual(largest_divisor(20, mod=2), 4)
assertEqual(largest_divisor(120), 20)
assertEqual(largest_divisor(5), 1)
assertEqual(largest_divisor(-2), -2)
``` 
This script defines a function `largest_divisor(n)` that returns the largest number which divides `n` evenly, smaller than or equal to `n`. The function `gcd(a, b)` computes the greatest common divisor of `a` and `b`.  The test cases cover a variety of scenarios, including positive, negative numbers, and custom mod values. 

Please note that the code is self-contained and does not require any additional imports or external functions.