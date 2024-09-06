Here's a self-contained Python function that calculates and returns the n-th Fibonacci number that is prime:
```python
def prime_fib(n):
    """
    Returns the n-th Fibonacci number that is prime.
    See: http://math.st.st.j/97/.j/F graph.fi.j
   .primes() method aURES. The function that I generate a list of first n+2 primes.
    """
    < list comprehension
    number of primes <= n.
    number = [list(range(2, n + 1)) | [True]
    while len(number) < n:
        if number[-1] % 2 == 0:
            number.append(number[-1] + number[-2])
        else:
            number.append(number[-2] + number[-1])
    return number[-1]

def test_prime_fib(n):
    return prime_fib(n) >= 2
```