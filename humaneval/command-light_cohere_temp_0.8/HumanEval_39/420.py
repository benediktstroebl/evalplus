```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    temp = prime_fib(n // 3)
    if temp == 0:
        return temp
    return temp + 1
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number that is also prime, and tests if the result is indeed prime by checking divisibility by 2 and 3. It recursively calls the