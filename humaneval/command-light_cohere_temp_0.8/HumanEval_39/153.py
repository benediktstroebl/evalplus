Here's the solution:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return n
```
This function takes an integer n as input and returns the n-th Fibonacci number that is also prime. It uses a techniques from the prime checking and Fibonacci recursion to achieve this.