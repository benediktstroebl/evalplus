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
``` 
This function `is_prime` takes an integer `n` as input and checks whether it is a prime number. The function uses an optimized algorithm to check for primality by using the `i` square pattern until the square exceeds the given number. 
This method is efficient and has a time complexity of O(sqrt(n)).