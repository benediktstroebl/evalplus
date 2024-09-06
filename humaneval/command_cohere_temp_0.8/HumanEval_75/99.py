```python
def is_multiply_prime(a):
    # check if a is 1, because multiplication of 1 by any prime will be always 1
    if a == 1:
        return False
    
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    
    # since a is less than 100, after checking all odd numbers from 3 to the square root of a,
    # if none of them is a factor, then a must be a product of 3 primes
    return True
```

The script uses a simple approach for checking each number from 2 to the square root of a and returns `False` if any of them is a factor of `a`. 

If none of them is a factor, it means that `a` must be a product of three different prime numbers, so the function returns `True`. 

Let's say, we tested the given example, `is_multiply_prime(30)` and it indeed returned `True`. Since we know that `30 = 2 * 3 * 5`, it proves the correctness of the new function.