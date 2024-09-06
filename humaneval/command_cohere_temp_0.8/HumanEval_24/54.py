```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through factors of `n` in the range of `1` to `n` and returns the maximum factor it finds. 
It is important to note that this method is not the most efficient approach for larger numbers, as it involves checking each potential factor up to `n`. Other methods involving prime factorization or mathematical optimizations could offer better performance for larger `n`. It is worth considering these approaches if the focus is on optimizing for speed rather than simplicity and clarity, as is the case in the provided solution.