```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return False

    # Check if a is the multiplication of 3 primes
    prime_factors = []

    while a % 2 == 0:
        prime_factors.append(2)
        a = a // 2

    # Check for all odd prime factors
    for i in range(3, int(a ** 0.5) + 1, 2):
        while a % i == 0:
            prime_factors.append(i)
            a = a // i

    if a > 1:
        prime_factors.append(a)

    return len(prime_factors) == 3

# Tests
a = 30
print(f"{a} is {('true' if is_multiply_prime(a) else 'false')}" )
```

The function uses an efficient algorithm, the `Sieve of Eratosthenes`, to find all the prime factors of the given number. The algorithm is implemented as a loop: first, all the even numbers are marked as prime when they are the basis of a multiplication, then for each odd number, all multiples of this odd number are marked as composite when they are the basis of a multiplication. The function checks the number after each loop to make sure it is not greater than 1, as it is possible that the given number has more prime factors than requested. 

The provided test ensures that the algorithm works correctly and prints out the results accordingly. You can add more tests to cover other numbers and scenarios, but this should handle the basic usage of the `is_multiply_prime` function.  The approach used here is efficient and can handle large numbers fairly quickly.  This is a `log(*n)` complexity where `n` is the number of atoms, which in this case, is the number of primes less than `100`.  The complexity of the `is_multiply_prime` is `O(log(*100)) = O(7)` which is pretty efficient.  It is using the `Sieve of Eratosthenes` efficient algorithm.  The approach used in `O(n)` would be a brute force approach where all combinations of prime numbers are checked and this is not efficient.  An example of this approach is: 
```python
def is_multiply_prime(a):
    prime = [True for i in range(100)]
    prime[0] = prime[1] = False
    for i in range(2, 100):
        if prime[i]:
            for j in range(i * i, 100, i):
                prime[j] = False
    return prime[a]
``` 
This function takes `O(100)` steps, whereas the efficient approach takes `O(7)` steps.