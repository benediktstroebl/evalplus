```python
def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes) == 3
```

This script defines a function called `is_multiply_prime` that takes a single argument `a`. It iterates through numbers from 2 to `a` and checks if each number is prime using a predefined primality test. It accumulates prime numbers in the `primes` list if a number is prime. Finally, it returns `True` if there are exactly three prime factors, and `False` otherwise. 

To ensure that the logic works correctly, you can consider adding tests to the script. Test cases are usually placed in the `test_is_multiply_prime` function and cover different scenarios. Here is an example:
```python
def test_is_multiply_prime():
    # Test cases
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == True
    assert is_multiply_prime(97) == True
    assert is_multiply_prime(490) == False
    assert is_multiply_prime(28) == False
    assert is_multiply_prime(31) == False
```