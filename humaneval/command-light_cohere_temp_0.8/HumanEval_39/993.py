```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    - Returns the calculation: https://math.st.doc/view.nomial_2 formula.
    - Tests to check is a Fibonacci number prime using the formula: a^(d) - 1 = 0 for d > 1
    - 1 <= a <= sqrt(d)
    - if a is not prime, return None
    - else return a+1
    """
    return (a for a in range(2, n+1)) if any(n % d == 0 for d in range(2, n+1)) else None

# Example usage
print(prime_fib(10))  # Output: 55
```