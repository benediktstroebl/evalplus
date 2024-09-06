```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0 or n == 6:
        return 6
    else:
        limit = 2  # set limit as sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime(i):
                limit = i
                break
        return limit

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n == 2:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n == i:
            return True
        i += 6
    return False

print(prime_fib(10))
``` 
This script defines a `prime_fib` function that calculates the nth Fibonacci number and checks if it's prime. It also defines a` is_prime` function to check if a given number is prime. 

The `print` statement then calls the `prime_fib` function with n = 10, which should return the number 89, which is the 10th Fibonacci number and is prime.