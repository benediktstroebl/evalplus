```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        if n % 2 == 0:
            return prime_fib(n - 2)
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return i
                i += 1
            return i + 2  # returned by convention
```
The function returns the n-th Fibonacci number that is also prime, by testing for divisibility by 2 and other numbers less than or equal to the square of the candidate number.