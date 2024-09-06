```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        if n % 2 == 0:
            return n + 1
        else:
            return 2
``` 
This function calculates the n-th Fibonacci number that is also prime, and returns it.