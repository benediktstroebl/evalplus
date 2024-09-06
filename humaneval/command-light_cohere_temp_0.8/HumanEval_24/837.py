```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer divisor of n, smaller than n."""
    while True:
        div = 1
        while div <= n:
            if n % div == 0:
                break
        div += 1
    return div
```  The code above defines a function `largest_divisor` that finds the largest integer divisor of a given number `n`. 

Here, it iterates until finding a divisor and returns the largest divisor found.