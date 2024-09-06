```python
def is_prime(n):
    """
    A recursive function to check if a number is prime. 
    Returns True if the Function: Prints False if the number is not prime, True otherwise.
    """
    means:
    1. If the number is 1 or not prime, return False. 
    2. If the number is odd, return False. 
    3. If the number is even prime for any even number of factors (except 1 and the number itself), 
    return True.
    """
test: 
    assert is_prime(6) == False
    assert is_prime(101) == True
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    ```