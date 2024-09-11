### Prime Fibonacci Numbers

The following Python script calculates the n-th number in the Fibonacci sequence that is also a prime number.

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num: The number to check.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Returns the n-th Fibonacci number.
    
    Args:
    n: The index of the Fibonacci number to return.
    
    Returns:
    The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number in the Fibonacci sequence that is also prime.
    
    Args:
    n: The index of the Fibonacci number to return.
    
    Returns:
    The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 0
    i = 0
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
            num = fib_num
            if count == n:
                return num
        i += 1


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script consists of three functions:

* `is_prime(num)`: Checks if a number is prime by testing divisibility up to the square root of the number.
* `fibonacci(n)`: Calculates the n-th Fibonacci number using an iterative approach.
* `prime_fib(n)`: Finds the n-th Fibonacci number that is also prime by iterating through Fibonacci numbers and checking if they are prime.

The example usage at the end demonstrates how to use the `prime_fib` function to calculate the first five prime Fibonacci numbers.