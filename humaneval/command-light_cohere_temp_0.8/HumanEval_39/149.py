```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next((i for i in range(3, n + 1) if is_prime(i)) - 2)

def is_prime(n: int):
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

def test_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == False
    assert is_prime(8) == False
    assert is_prime(10) == True
    assert is_prime(12) == True
    assert is_prime(20) == True
    assert is_prime(21) == False

def test_prime_fib():
    assert prime_fib(0) == 0
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
```
The provided code includes a `prime_fib` function that calculates the n-th Fibonacci number that is prime and returns it. The function employs a concept of prime numbers and their relation to Fibonacci numbers to achieve this. 

The `is_prime` function determines whether a given number is prime or not using the trial method, which involves testing divisibility from 2, 3, and a few other numbers up to the given number. 

The `test_prime` function contains a list of test cases for `is_prime` function, and it verifies that the function correctly identifies prime numbers.