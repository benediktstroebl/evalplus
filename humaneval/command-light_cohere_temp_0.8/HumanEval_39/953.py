```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0:
        return True
    else:
        a, b = 5, 2
        while b <= n:
            a, b = b, a + b
            if a > 1 and a % 1 == 0 and b > 1 and b % 1 == 0:
                return True
        return False
``` 
This function, `prime_fib`, is a recursive implementation of the Fibonacci number and primality test. It returns `True` if the important Fibonacci numbers are prime, and False otherwise.