```python
def prime_fib(n: int):
    """
    This function returns the n-th number that is a Fibonacci number and is also prime.

    A Fibonacci number is a sequence of numbers where each successive number is the sum of the two preceding ones, is defined as 0, 1, 1, 2, 3, 5, ... etc. A Fibonacci number that is prime if its only positive divisors are itself and 1.

    Returns n times Fibonacci number that is not a prime, or a negative number, returns None.
    """
    return _ prime_fib_recursive(n, 2) if n <= 0 else next((n-1) if n % 2 == 0 else (n-2)) + 2

def prime_fib_recursive(n: int, memo={}):
    """
    Recursive function that returns the n-th Fibonacci number is also prime.

    The function uses memoization to avoid redundant calculations.

    If implementation uses the general recursion to calculate the n-th Fibonacci number.

    Returns the x, the n-th Fibonacci number that is prime, or -1 if it is not a prime or a negative number.

    """
    return memo.get(n,n, (n <= 0 or n < 2)
)
get(n, 0)

def test_prime_fib():
    """
    Test the function
    """
    print(prime_fib(5))
```