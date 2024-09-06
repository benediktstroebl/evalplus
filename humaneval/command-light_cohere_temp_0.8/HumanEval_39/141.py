```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        a, b = 3, 5
        for _ in range(2, n):
            if a % b == 0:
                return a
            a, b = b, a + b
        return a
``` 
This Python function, `prime_fib`, calculates the n-th Fibonacci number that is prime and returns it. The function starts by checking if `n` is less than or equal to 1. If so, it returns `n` itself, as it is not a valid input for the Fibonacci sequence. The function then checks if `n` is even. If `n` is even, it returns `2` since both 1 and 2 are prime. 

If `n` is odd, the function then initializes variables `a` and `b` with values 3 and 5 respectively, and enters a loop that iterates from 2 to `n` times. In each iteration, it checks if `a % b == 0`, which would make it a prime number. The function then updates the values of `a` and `b` to `b` and `a + b` respectively. 

Finally, the function returns the value of `a`, which is the n-th prime Fibonacci number.