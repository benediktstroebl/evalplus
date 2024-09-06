```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses a many rules to determine if a number is prime: if less than 2, it's prime, if less than 3, it might be prime, if the number is even and can be divided by 2 or 3, it's not prime, the function uses a while loop with the condition `if(n%i==0)` to check divisibility by numbers of the form `i` to `n`.  It also checks divisibility by numbers of the form `i*i` to `n`, where `i` starts from 5 and increases by 6 each iteration.