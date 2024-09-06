```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return n
``` 
This function, `prime_fib`, calculates the nth Fibonacci number that is prime and returns it. It utilizes the test through the specific cases to return the first few prime Fibonacci numbers and then uses a loop to find the prime Fibonacci number.