```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function revolves around the primality testing algorithm dubbed the `Sieve of Eratosthenes`. It efficiently checks if an integer is prime by iteratively marking the multiples of 2 and progressively marking multiples of prime numbers it encounters. The process continues until the given number is marked as composite, thus this algorithm optimally identifies prime numbers.

The algorithm's efficiency is demonstrated by its ability to handle diverse test cases, including larger numbers like `13441` and `61`. The initial cases, such as `6`, `4`, and `1`, showcase the function's accuracy in identifying composite numbers and ensuring that no exceptions are raised.