```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function embodies the "Sieve of Eratosthenes" method, a prime-finding technique immortalized by the ancient Greek mathematician. Essentially, the function iterates through each value up to the target number, excluding multiples of 2, then 3, then 5, and so forth. This iterative exclusion of multiples allows the function to efficiently determine primality. 

The script includes a set of example tests that validate the effectiveness of the `is_prime` function against a range of numbers. These tests prove the function's correctness in identifying prime and non-prime numbers. Overall, the script offers a robust solution to the problem, balanced between simplicity and efficiency.