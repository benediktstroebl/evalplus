```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes a number `n` as input and iterates through all numbers from 1 to `n` (inclusive). During each iteration, it checks if the current number `i` can divide `n` evenly. This is done by using the modulo operator '%' which returns the remainder when `n` is divided by `i`. If there is no remainder, it means that `i` is a divisor of `n`, and since we are interested in the largest divisor, we return `i` instantly. The loop continues until all numbers from 1 to `n` are checked, guaranteeing that the first valid divisor encountered is the largest divisor smaller than `n`.