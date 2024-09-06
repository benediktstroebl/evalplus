```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test case:
n = 15
print(largest_divisor(n))
``` 
This code defines a function `largest_divisor(n)` that calculates the largest integer that evenly divides a given number `n`. The function achieves this by using the `gcd()` function to find the greatest common divisor of `n - 1` and `n - 2`, and then divides `n` by this result. 

The function is then tested with a value of `n = 15` and the result is printed, which should be `5`.