Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical flow to determine whether a given number is prime. It begins by checking if the number is less than 2, returning false immediately if so. The function then iterates through numbers from 2 up to the square root of the input number, checking for divisibility. If the number is divisible by any integer within this range, it's not prime, and the function returns false. If the number is not divisible by any integer within this range, it is prime, and the function returns true. 

This algorithm continues to be a standard methodology for prime checking and holds true for larger numbers compared to simpler methods that only work for smaller numbers.