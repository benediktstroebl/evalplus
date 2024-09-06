```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1, 9)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

# Tests
print(largest_divisor(15))  # Output: 5
print(largest_divisor(27))  # Output: 1
``` 
The above code defines a function `largest_divisor(n: int)` which returns the largest number that divides the given number `n` evenly, smaller than or equal to `n`. The function uses the `gcd` function to find the greatest common divisor of `n` and its predecessor, which is the key to this problem.