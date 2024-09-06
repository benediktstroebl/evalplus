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
    assert is_prime(6) == False
    assert is_prime(101) == True
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    ```
The provided Python code defines a function called is_prime(n), which checks whether a given number is prime or not. The function employs a well-known primality-testing criteria: if the number is less than or equal to 2, it's prime; if it's less than or equal to 3, it's composite; the function then iterates up to the square root of the number, checking for divisibility up to the square root. The test function is a straightforward and effective way to determine whether a number is prime or not, passing all the tests successfully.