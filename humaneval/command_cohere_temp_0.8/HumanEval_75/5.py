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

This script checks if the given number `a` is the product of three primes by iterating from 2 to `a` and checking if each number is prime. A number is prime if it has exactly two distinct positive divisors, namely 1 and itself. 

It utilizes a simple optimization: it checks only up to the square root of the number `i`. Thus, it excludes the needless checking of the divisors of the form `i + k * 1000`, where `k` is also a divisor of `i`. If the number is prime, it adds it to the `primes` list, and returns `True` if the list has exactly three elements, indicating that the given number is the product of three primes. 

To ensure accuracy, test the code on a variety of test inputs, including large and small numbers. You may verify the script's correctness and behavior by adding tests like these:
```python
# Tests:
assert is_multiply_prime(30)
assert not is_multiply_prime(28)
assert is_multiply_prime(52)
assert not is_multiply_prime(501)
``` 
This will ensure the function's correctness and its behavior for a range of inputs.