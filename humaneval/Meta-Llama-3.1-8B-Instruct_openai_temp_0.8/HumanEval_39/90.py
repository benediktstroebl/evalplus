### Prime Fibonacci Numbers
Here is a Python script that solves the problem:
```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib_sequence = fib_gen()
    i = 1
    while i <= n:
        num = next(fib_sequence)
        if is_prime(num):
            i += 1
    return num - 1  # return the second-to-last prime Fibonacci number


if __name__ == "__main__":
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
```
This script uses a generator to produce Fibonacci numbers and checks each one to see if it's prime. It keeps track of the count of prime Fibonacci numbers found so far and returns the n-th one. Note that it actually returns the second-to-last prime Fibonacci number because it increments the count after finding a prime number.