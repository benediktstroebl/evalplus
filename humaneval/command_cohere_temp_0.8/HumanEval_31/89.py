```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function incorporates the necessary logic to determine whether a given number is prime. It begins by checking if the number is less than 2, returning False if so, as numbers less than 2 are not prime. The function then starts a loop from 2 and goes up to n-1. If the number is divisible by any integer within this range, it's not prime, and the function returns False. However, if the number isn't divisible by any integer within this range, it's prime, and the function returns True. 

This approach allows the function to efficiently determine a number's primality based on fundamental prime determination principles.