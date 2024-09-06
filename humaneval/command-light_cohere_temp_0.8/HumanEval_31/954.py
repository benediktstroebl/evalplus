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
    print(is_prime(6))
    print(is_prime(101))
    print(is_prime(11))
    print(is_prime(13441))
    print(is_prime(61))
    print(is_prime(4)))
    print(is_prime(1)))

test()
```
The above Python function, `is_prime`, returns True if the input number is prime, and False otherwise. It uses a specific logic to determine whether a number is prime or not. The test function is used to run the `is_prime` function with various inputs and verify the correctness of the function.