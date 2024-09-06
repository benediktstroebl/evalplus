Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning False if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns False. However, if neither condition is met until the end of the iteration, it returns True, indicating that the number is prime. 

This solution corresponds to the provided example in the prompt and should pass the tests given. 
Here is an example of how you might test this function:
```python
# Test case for is_prime
def test_is_prime():
    assert is_prime(101) == True
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(6) == False
    assert is_prime(4) == False
    assert is_prime(1) == False
``` 

This would provide thorough testing for the function, which should help ensure that it corresponds to the provided specification. 
Let me know if I can help with anything else!