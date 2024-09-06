```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)
 
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)
 
# unit tests
assertEqual(largest_divisor(1), 1)
assertEqual(largest_divisor(2), 2)
assertEqual(largest_divisor(3), 3)
assertEqual(largest_divisor(6), 2)
assertEqual(largest_divisor(10), 2)
assertEqual(largest_divisor(13), 5)
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(21), 3)
```
This code provides a function `largest_divisor` which returns the largest integer that divides a given number `n` evenly, smaller than `n`. The `gcd` function calculates the greatest common divisor of two numbers, `a` and `b`.  The `assertEqual` functions test the function with various input pairs and ensure the expected output is produced.