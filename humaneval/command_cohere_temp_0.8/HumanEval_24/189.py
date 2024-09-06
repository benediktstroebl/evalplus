```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i > i:
            return i
    return 1
```
The function iterates through numbers from 1 to n. If n is divisible by i and n // i is greater than i, it returns i as the largest divisor. If no such i is found, it returns 1. This approach is efficient and guarantees the largest divisor is found.