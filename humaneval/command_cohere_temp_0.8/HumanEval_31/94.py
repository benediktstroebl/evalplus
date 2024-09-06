Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function checks if a given number `n` is less than 2, returns `False`. If `n` is greater than or equal to 2, it iterates from 2 to the square root of `n` (inclusive), and for each iteration, it checks if the given number is divisible by the current number on the loop. If it is, it returns `False`. If the loop completes without finding a divisor, it returns `True`.

This solution should produce the following outputs when the provided specific test cases are called:
```
False
True
True
True
True
False
False
``` 

**NOTE:** This approach has a time complexity of O(sqrt(n)), meaning it checks up to the square root of the number in each direction. This is a pretty efficient approach, but there are more advanced prime-checking algorithms for checking larger datasets.