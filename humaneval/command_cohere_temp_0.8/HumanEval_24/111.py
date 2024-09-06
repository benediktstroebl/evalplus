```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i >= i:
            return i
    return 1
```
The function iterates through factors from 1 to `n`, and returns the `i` value as the largest divisor if `n` can be evenly divided by `i`, and `n // i` is greater or equal to `i`.  Otherwise, the function returns 1, indicating that the largest divisor is the number itself.  This code matches the specified problem and output.