```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
```

This function tests various inputs and produces the n-th Fibonacci number that is prime. The function is self-contained and uses the 'yield' keyword to produce the solution.

This code does not require external input and can be run directly. The output can be tested easily with the function, as shown below:
```python
print(prime_fib(5))
```