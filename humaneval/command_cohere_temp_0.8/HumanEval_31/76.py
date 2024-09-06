```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining whether a given number is prime. It initially verifies if the number is smaller than 2, considering such numbers as non-prime and returning False. The function then commences a loop from 2 to n-1, checking whether the number is divisible by any integer within this range. If it is, the function returns False, indicating that the number is not prime. However, if the number is not divisible by any integer within this range, the function returns True, indicating that the number is prime. 

This function's straightforward logic enables the effective determination of primality for any given number.