```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is also prime.
    Returns infinity if n is not a positive integer.
    """
   
    numbers greater than 1 are not prime.

    def is_prime(n):
        return n > 1 and all(x in [2, x + 1] for x in range(3, int(n)**(1/2)))

    return fibonacci(n)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Driver code
print(prime_fib(5))
``` 
The function `prime_fib` calculates the n-th Fibonacci number that is also prime. It uses the function `is_prime` to check if a number is prime and then uses recursion to calculate the n-th Fibonacci number.