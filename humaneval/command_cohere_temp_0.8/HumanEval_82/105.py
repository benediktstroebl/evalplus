```python
def is_prime_length(input_str):
    if len(input_str) <= 1:
        return False
    for i in range(2, int(len(input_str)**0.5) + 1):
        if len(input_str) % i == 0:
            return False
    return True
```

This function `is_prime_length` checks if the length of the provided string is a prime number or not. The basic flow follows these steps:
1. If the length of the string is 1 or less, it obviously isn't prime, so the function returns False.
2. The function iterates from 2 to the square root of the length of the string. This is based on the optimization that primes greater than the square root of the number can be ignored.
3. For each number `i` in that range, if the length of the string is divisible by `i`, it returns False since it is not a prime length.
4. If no divisors are found in the loop, it returns True, indicating that the length is a prime number. 

This should correctly solve the problem for various cases of strings provided.