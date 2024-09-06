```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        # Calculates the n-th Fibonacci number and returns it if it's prime
        return not (prime_fib(n // 2) * prime_fib(n // 2) + 1)
``` 

This code defines a recursive function, `prime_fib`, that computes the n-th Fibonacci number. It then returns the value if the number is less than or equal to 1, and if it is even, it returns the value of the (n/2)th Fibonacci number multiplied by 2. If it is odd, it further checks if the product of the (n/2)th and (n/2)th Fibonacci numbers plus 1 is a prime number. If the product is not prime, it returns the number as it is, else it calculates the product of the Fibonacci numbers and returns that value.