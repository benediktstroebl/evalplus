```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a = b
            b += 1
    c = a
    d = 2
    while d <= a:
        if is_prime(d):
            break
        d += 1
    if d > a:
        return a
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# Example usage
print(prime_fib(5))
``` 
This code defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime. The function uses a `is_prime` helper function to check primality. The `is_prime` function uses a trial and error approach to determine if a number is prime or not. 

The example usage demonstrates how to call the `prime_fib` function with an input of 5 and prints the result, which should be the 89th Fibonacci number.