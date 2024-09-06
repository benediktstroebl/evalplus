```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(27) == 3
assert largest_divisor(6) == 2
assert largest_divisor(12) == 4
```  This code defines a function **largest_divisor** that calculates the largest integer dividing a given number evenly, smaller than the given number **n**. The function uses the **gcd** function to find the greatest common divisor of n - 1 and n - 2, which is equal to the largest integer dividing n evenly. 

The function then tests with different input values and asserts that the result of **largest_divisor** is equal to the expected value.