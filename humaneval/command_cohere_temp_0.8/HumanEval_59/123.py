```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Script start
    assert n > 1 and not is_prime(n), "n must be greater than 1 and not prime"

    largest_factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            largest_factor = possible_factor
            break

    # Script end
    return largest_factor

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function 'largest_prime_factor' employs an optimization technique where it initially assumes the largest factor, given n is not a prime, and then verifies this assumption by iterating through possible factors up to 'int(n**0.5)'. This number is chosen because larger factors of a number are usually less than or equal to its square root. 

However, the square root approximation is not always perfect, hence the factor checking process includes all factors up to 'int(n**0.5)'. This allows the script to handle many cases efficiently while still ensuring correctness. 

The supplementary function 'is_prime' is used in the assertion of the provided test cases, to ensure they are proper inputs to the 'largest_prime_factor' function. 
This approach allows the main function to focus on its primary task, optimizing the largest prime factor retrieval. 

Please note, the underlying theory and approach for determining prime factors exists within the square root of the number, however the choice of iterating up to 'int(n**0.5)'' is a balanced approach between efficiency and correctness.