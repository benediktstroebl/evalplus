```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that evenly divides n, 
    less than n.
    """
    return n //gcd(n)
```

Here, the function uses the gcd function from the math module to calculate the greatest common divisor of two numbers. 

The gcd of two numbers a and b is the product of all the prime factors that are common in the two numbers.

In this case, the function returns the gcd of n and 1 since 1 is the only number that divides n evenly.