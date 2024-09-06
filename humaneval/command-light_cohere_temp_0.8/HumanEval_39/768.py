```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.
    Returns None if n < 0 or
    Returns an error tuple if not a prime Fibonacci number.
    """
    generates and checks whether a Fibonacci number is prime:
    if n == 1:
        return 2
    elif (n%1) == 0:
        return None
    else:
        temp = prime_fib(n // 2)
        if temp is not None:
            return temp
        
# Example usage
print(prime_fib(5))
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number and checks if it's prime. The function returns `None` if n is 0, and returns an error tuple if the number is not a prime Fibonacci number. The result is then tested with the `print(prime_fib(5))` statement.