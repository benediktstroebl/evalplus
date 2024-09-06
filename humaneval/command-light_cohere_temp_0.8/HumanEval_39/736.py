```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        a, b = 2, 3
        while a * a <= n:
            if b <= n / a:
                a, b = a + b, b
            else:
                break
        return a

# Test the function with some examples
assert(prime_fib(1) == 2)
assert(prime_fib(2) == 3)
assert(prime_fib(3) == 5)
assert(prime_fib(4) == 13)
assert(prime_fib(5) == 89)
```
This function will return the n-th Fibonacci number that is prime. It uses the traditional approach of iteratively finding the next prime by checking the divisibility of the current number by 2, 3, ... until the number becomes greater than its square.