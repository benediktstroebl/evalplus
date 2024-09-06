Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function defines a recursive function `is_prime` that checks if a given number `n` is prime or not. The function first checks if `n` is less than 2, considering such a number to be not prime, and thus returns False. For larger values of `n`, the function performs a loop from 2 to the square root of `n` (inclusive), and for each iteration, it checks whether the given number is divisible by any number in the range. If the condition is `n% i == 0`, the function returns `False` as the given number `n` is not prime. The loop ends for all values `i` for which this condition holds. If no such divisors are found after having looped through all values, the function returns `True`, indicating that the given number is prime. 

This solution corresponds to the specification included in the original prompt, as the function passes the provided example tests. 
```python
# Tests
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```