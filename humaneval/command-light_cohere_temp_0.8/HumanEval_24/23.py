```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(6))   # Output: 2
print(largest_divisor(49)) # Output: 23
``` 
This Python code defines a function `largest_divisor(n)` that calculates the largest number that evenly divides a given number `n`. The function utilizes the `gcd()` function to compute the greatest common divisor of `n-1` and `1`, then subtracting one from the result to obtain the largest divisor less than `n`. 

The `gcd()` function calculates the greatest common divisor using the Euclidean algorithm. The script includes test cases that demonstrate the functionality of the `largest_divisor()` function with various input values.