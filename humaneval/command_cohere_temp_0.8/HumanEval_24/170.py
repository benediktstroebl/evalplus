```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i >= i:
            return i
    return 1
```
The function iterates through numbers from 1 to n. If `n` is divisible by `i`, it checks if the quotient of the division is greater than or equal to `i`. If so, it returns `i` as it is the largest divisor that meets the criteria. If no such integer is found, it returns 1, which is the default return value for the function.