```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        prime = prime_fib(n // 2)
        return prime + next((i for i in range(2, n) if is_prime(i)) - 1)

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
    for num in range(1, 10):
        if is_prime(num):
            print(f"{num} is a prime")
        else:
            print(f"{num} is not a prime")

test_prime()
prime_fib(1)
prime_fib(2)
prime_fib(3)
prime_fib(4)
prime_fib(5)
print()

```
This Python script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime. The function uses a simple backtracking algorithm. It first checks if `n` is less than or equal to 1, in which case it returns `n`. The function then checks if `n` is even and returns the result of `prime_fib(n // 2) + 2`. If `n` is odd, it uses the `prime_fib(n // 2)` function to continue the sequence and add 1 to the result. The function also uses a `is_prime` function to check if `n` is prime.  The function uses a `next` function with a generator expression `(i for i in range(2, n) if is_prime(i)) - 1` to get all the primes less than or equal to `n`.  The `is_prime` function uses a simple algorithm to check if `n` is prime, and returns `True` if `n` is a prime number and `False` otherwise.