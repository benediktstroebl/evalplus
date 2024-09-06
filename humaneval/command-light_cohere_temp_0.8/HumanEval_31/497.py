```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
def test_is_prime():
    assert is_prime(6) == True
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(61) == True
    assert is_prime(9) == False
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == False
    assert is_prime(12) == False
    assert is_prime(13441) == True
    assert is_prime(6459) == False

# Main function
def main():
    test_is_prime()

if __name__ == "__main__":
    main()
```
The function is_prime checks if a given number is prime or not. It starts by checking small numbers and then uses an efficient square root checking mechanism to check for primality. The function also uses a divide-by-mod approach with small primes to check for primality, which reduces the number of iterations needed.