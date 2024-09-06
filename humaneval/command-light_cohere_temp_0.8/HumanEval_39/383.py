```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    result = 0
    for i in range(5, n + 2, 6):
        if i % 2 == 0 or i % 3 == 0:
            continue
        result = (result + i) // 2
    return result
``` 
This function calculates the n-th Fibonacci number that is also prime, and tests if it passes the test using the given input n.