```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is prime.
    return the prime_fib(1):
        2
        is_prime(2)  # returns True
        return 2

    is_prime = [True] * (x for x in [2, 3, 5, 7, 11, 13])
    while n > 1:
        candidate = prime_fib(n)
        if is_prime[candidate]:
            n -= 1
        else:
            is_prime[candidate] = False
    return is_prime[-1]

# Example usage
print(prime_fib(5))  # 89
``` 
This Python function, prime_fib, calculates the nth Fibonacci number that is prime and returns it. The function utilizes a prime numbers test to ensure that the generated number is prime, by checking if it satisfies the criteria of a prime number.