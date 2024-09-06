Here is a Python script with a self-contained function that solves the problem of checking whether a given number is a prime:
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
This function takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It uses a i` different heuristic to test for primality, and it can efficiently determine whether a number is prime or not. 
The time complexity of this function is O(sqrt(n)), where sqrt(n) represents the square root of the input number.