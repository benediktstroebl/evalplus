```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
The function iterates through numbers from 1 to n-1, checking if the number is divisible by n. The largest divisor is returned as soon as it is found.