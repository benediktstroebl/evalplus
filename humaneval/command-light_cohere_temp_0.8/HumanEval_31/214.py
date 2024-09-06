Here's a self-contained Python function that checks whether a given number is a prime:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True
```
This function checks the primality of the given number n by using a simple algorithm. It starts with `n` and iterates from 2 up to the square root of `n` (int(n ** 0.5)) + 1`. If there's a divisor, `i`, such that `n % i == 0`, it returns False, indicating that `n` is not a prime. 

This function is self-contained, and it does not rely on any external functions or modules. It can be easily used to solve the primality checking problem for any given number.