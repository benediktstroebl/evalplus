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
This Python function is_prime takes an integer n as input and checks whether it is prime or not. The function first handles some special cases: numbers less than or equal to 1 and numbers equal to 2 or 3. Then, it uses a simple optimization by checking divisibility up to the square root of the number. Finally, it iterates up basic sieve of Eratosthenes.