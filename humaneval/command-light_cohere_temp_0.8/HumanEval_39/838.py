```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        temp = prime_fib(n // 2)
        if temp == 2 or temp == 3:
            return temp
        else:
            # Find the square root of n
            square_root = int(n ** 0.5)
            # Check for multiples of square root until we find the first prime that exceeds n
            for i in range(square_root + 1):
                if is_prime(i):
                    return i
    return -1  # Return -1 if no prime is found

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_num = int(n ** 0.5)
    sqrt_num:
        for num in range(5, sqrt_num, 6):
            if n % num == 0:
                return False
    return True
```
The provided code contains a function called `prime_fib` which calculates the nth prime Fibonacci number, and also checks if it's prime. The code also includes a function `is_prime` which checks whether a given number is prime or not.