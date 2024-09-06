```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach via a loop that examines all integers from 2 up to the square root of the target number. If none of these integers divide the target, the function returns `True`, indicating that the number is prime. Conversely, if any divisor is found, the function returns `False`, suggesting that the number is not prime. 

The tests provided in the prompt return the expected outputs:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
``` 
This would be the expected output. If there's anything else I can help with, let me know! I can assist with additional examples or guidance if you'd like to expand the function's capabilities or optimize its algorithm. Feel free to ask if you have any questions!