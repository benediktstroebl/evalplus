```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes an integer n as input and returns the largest integer divisor of n that is smaller than n. It accomplishes this by iterating through all integers from 1 up to n itself. It then determines if the number n is divisible by i, using the modulo operator (`n % i`). If i is a divisor of n, it returns i. As soon as the loop completes its iteration without finding a suitable divisor, it returns n, which serves as the default solution.