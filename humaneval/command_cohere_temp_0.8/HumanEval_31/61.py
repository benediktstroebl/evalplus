```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
``` 

This function comprises a streamlined primality test for n, which checks for divisibility by all integers from 2 to the square root of n, returning False if any such divisor is found, and True otherwise. This method is optimal for its simplicity and computational efficiency.