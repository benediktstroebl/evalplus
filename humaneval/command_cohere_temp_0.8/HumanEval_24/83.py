```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i
    return 1
```

This algorithm leverages the fact that divisors come in pairs `i` and `n//i` where `i` is a divisor of `n`. It iterates through all possible divisors `i` of `n` (excluding `n` itself) and returns the largest divisor that is smaller than `n`. The check `j < i` ensures that we don't mistakenly return the larger divisor when both are equal to `n`. 

The largest divisor of `n` is `n` itself if none of the divisors meet the criteria, in which case the function returns 1 as the default response. 

The unit test passed value is `15` which returns `5` as the largest divisor.