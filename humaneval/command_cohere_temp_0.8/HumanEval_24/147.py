```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index `i` divides `n` evenly (i.e., `n % i == 0`), then that number is returned as the largest divisor. This handles the case where `n` is perfectly divisible by its smaller factors, ensuring we don't overlook any factors when seeking the largest divisor.