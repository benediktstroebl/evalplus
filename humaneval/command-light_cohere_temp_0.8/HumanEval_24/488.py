Here's the provided Python script:
```python
def largest_divisor(n: int) -> int:
    return next(six.set(x) for x in range(2, n+1) if n % x == 0)
```
The function uses the set of numbers from 2 up to the input number n, then checks if there's any divisor using the modulo operator. The function returns the This particular number that is a divisor, or the input number itself if no divisors are found.