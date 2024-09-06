```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
``` 

This function adheres to the problem statement and satisfies the given tests, returning true for prime numbers and false otherwise. It first checks if the number is less than 2, deeming them non-prime and returning false in such cases. Then, it iterates from 2 to the square root of the number, checking for divisibility – if the number is divisible by any integer in this range, it's not prime, and the function returns false. If no divisors are found, the number is prime, and the function returns true. 

This approach is efficient because checking divisibility by numbers larger than the square root is unnecessary, and the time complexity of the function is O( √n ). It doesn't consider edge cases like 1, as it's not a prime number, but it's a logical exception that can be added if needed.