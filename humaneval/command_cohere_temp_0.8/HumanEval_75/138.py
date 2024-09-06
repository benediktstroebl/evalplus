```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return "Invalid input"

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

    if len(prime_factors) != 3:
        return False
    else:
        return True
```

The `is_multiply_prime` function implements an optimized brute force approach to determine if the number `a` is the product of three prime numbers. It first checks if a is less than 100 to validate the input. It then checks for an even factor twice, speeding up the process. It then iterates through all odd prime candidates, starting from 3 up to the square root of a. Once all prime factors are found, the function confirms that their length equals three to confirm the desired condition. 

The `is_multiply_prime` function should ideally be used with validation for real-world scenarios, even though the provided `if a > 100` serves as a basic preliminary check. 

This approach proves to be efficient in code terms of size and performance, showcasing the elegance of mathematical reasoning in practical programming.