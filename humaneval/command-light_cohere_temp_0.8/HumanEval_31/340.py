```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test function
def test():
    print("Result:", end="flush, n_is_prime(12))
    print("Results:", end="flush, n_is_prime(6))
    print("All primes:", end="flush, n_is_prime(7))

# Test various inputs
test()
``` 
In this script, the function is_prime(n) takes an integer n as input and checks whether it's a prime number or not. It uses a correct trial and verification logic, which is self-contained within the function. The test function is used to test the correctness of the is_prime function with various inputs.