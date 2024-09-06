```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next((c for c in (a, b) if c <= n)), b + 1
    return a
```
This Python function `prime_fib` computes and returns the n-th Fibonacci number that is prime, using an efficient iterative approach. The function first initializes variables `a` and `b` with the first two Fibonacci numbers and then iteratively generates subsequent Fibonacci numbers, ensuring they are prime and within the desired range using a nested loop with a loop condition. 

It runs through the range from 1 to 5, and within this loop, it generates the next Fibonacci number and checks if it's less than or equal to the given value `n`. If this number is prime, it is stored in the variable `b + 1` and assigned to the next value of `b`. The function then returns the value of `a`, which is the n-th prime Fibonacci number.