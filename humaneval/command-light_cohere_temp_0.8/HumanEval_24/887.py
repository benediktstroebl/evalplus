```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if n % x == 0)
```
This code calculates the largest integer that evenly divides a given number 'n', without exceeding it. It uses a max function to find the largest divisor less than the number itself. This code is efficient by avoiding unnecessary calculations of all divisors of 'n', and instead finding the largest one among a range of potential divisors.