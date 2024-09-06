```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer that evenly divides the given number"""
    if n <= 0:
        raise ValueError("The input number must be a positive integer.")
    divs = 0
    while n % 2 == 0:
        divs += 1
        n //= 2
    if n > 1:
        divs += 1
        n //= 3
    return divs
``` 
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the number of its largest divisors. It does so by iterating through 2, then 3, and so on up to the square root of 2, then returns the number of divisors found.