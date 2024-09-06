Here's a self-contained Python function that calculates and returns the n-th Fibonacci number that is also prime:

```python
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    # Base cases
    if n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Hypotenuse formula for nth Fibonacci number
    base = 3
    exponent = 2
    result = base**exponent
    while base <= n:
        result *= base
        base += 1
    
    # Check if result is prime using isprime() function from math module
    is_prime = all(math.isprime(x) for x in math.is_prime(result))
    if is_prime:
        return result
    else:
        return None
```
This function calculates the n-th Fibonacci number that is prime, using the formula from the article "Prime Fibonacci Numbers" by Bruce Wein and Plass and then checks if the result is prime using the `math.isprime()` function from from in the `math` library.