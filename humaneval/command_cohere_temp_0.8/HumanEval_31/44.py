```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes an integer `n` as input and checks if it is prime or not. It employs a straightforward algorithm that iterates through the integers from 2 up to the square root of `n`, checking whether `n` is divisible by any of them. If `n` is divisible by any of these integers, it is not prime, and the function returns `False`. If `n` is not divisible by any of them, it is prime, and the function returns `True`. 

This algorithm is relatively efficient because it only needs to iterate up to the square root of `n`. Additionally, since the maximum index `int(n ** 0.5) + 1` in the loop is never exceeded, it doesn't require an aggressive optimization strategy like MPI (Matthews' Primality Infrastructure) or a sophisticated mathematical derivation like the Miller-Rabin primality test. 

Note that this function assumes that the input is a positive integer. If the input is negative or not an integer, the function may return unexpected results. 

This function should correspond to the provided tests and produce the following outputs:
```
True
False
True
True
True
False
False
``` 
If you'd like to include additional tests or enhance the function's robustness, I can provide some suggestions and variations.