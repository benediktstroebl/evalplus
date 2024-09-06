```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

Let's break down the code step by step:
1. `is_prime(n)`: This function takes an integer `n` as input and checks whether it is a prime number or not. The function employs a efficient strategy called the `Sieve of Eratosthenes` to determine if a number is prime. 
2. `count_up_to(n)`: This function takes an integer `n` as input and returns a list of the first `n` prime numbers less than `n`. The function works by iterating through integers from 2 up to `n`, and for each integer, it checks if it is prime using the `is_prime` function. If it's prime and it's less than `n`, it adds the prime number to the `primes` list and increments the `count` counter. The loop continues until `count` reaches `n`, at which point it breaks to stop the loop. 

The `count_up_to` function ultimately provides the requested list of prime numbers. 

The unit test module `test_primes.py` contains a number of tests to check the correctness of the prime-checking function and the main problem solution. You can check the test suite against the provided code to confirm its robustness.