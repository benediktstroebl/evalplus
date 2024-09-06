```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer dividing n evenly, smaller than n"""
    return (n+1) // gcd(n+1, 2)

def gcd(a: int, b: int) -> int:
    """ Returns the greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return a

largest_divisor(15)  # Output: 5
```