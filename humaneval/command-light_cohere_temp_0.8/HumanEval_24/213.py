```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
assertEqual(largest_divisor(1), 1)
assertEqual(largest_divisor(2), 2)
assertEqual(largest_divisor(3), 2)
assertEqual(largest_divisor(4), 2)
assertEqual(largest_divisor(5), 5)
assertEqual(largest_divisor(6), 2)
assertEqual(largest_divisor(12), 4)
assertEqual(largest_divisor(15), 5)
```
This code defines a function `largest_divisor(n)` that returns the largest number that divides `n` evenly, smaller than `n`. It uses the `gcd` function to calculate the greatest common divisor of `n - 1` and 1, and then it returns `(n - 1) // gcd(n - 1, 1)`, which is the largest divisor. The function is designed by directly using `gcd` instead of reimplementing it. 
Test cases are provided to verify the correctness of the `largest_divisor` function.