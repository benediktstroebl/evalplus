```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, less than or equal to n."""
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
```
This function, largest_divisor, takes an integer n as input and returns the largest integer that divides n without a remainder. It iterates through through numbers from 1 up to the square root of n, and checks if n is divisible by each of these numbers.