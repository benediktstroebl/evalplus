```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n + 1):
        if is_prime(i):
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

# Example usage
print(prime_fib(5))
``` 
This code defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it is prime. The function uses nested loops and a helper function `is_prime` to efficiently determine prime status. 

The `is_prime` function uses a loop with a maximum threshold and checks for divisibility by the numbers from 2 up to the square root of the number.