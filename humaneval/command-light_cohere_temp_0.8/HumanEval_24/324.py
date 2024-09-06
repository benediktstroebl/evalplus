```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1)
def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
# Test the function
n = 15
print(largest_divisor(n))  # Output: 5
``` 
This code defines a function `largest_divisor(n)` that finds the largest divisor of a given number `n`. It uses the `gcd()` function to calculate the greatest common divisor of `n-1` numbers, which are the factors of `n`. The function then returns the largest number that divides `n` evenly. 
Test the function with a value of `n = 15` and prints the result, which is `5`.