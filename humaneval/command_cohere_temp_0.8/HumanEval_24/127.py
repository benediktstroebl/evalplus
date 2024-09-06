```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i >= i:
            return i
    return 1
```
The function iterates through numbers from 1 to n. If n is divisible by i and the divisor i is equal to or larger than the floor of n/i, it returns i as the largest divisor. If no valid divisor is found, it returns 1 as the default outcome.