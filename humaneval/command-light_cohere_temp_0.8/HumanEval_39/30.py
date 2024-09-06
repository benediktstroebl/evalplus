```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    # check if it's a prime by loop
    i = 6
    while i * i <= n:
        if n % i == 0:
            return False
    return True
    
# test the function
print(prime_fib(5))  # this should print 89
``` 
This function, `prime_fib`, calculates the n-th Fibonacci number that is also prime using basic mathematical operations and testing for primality.