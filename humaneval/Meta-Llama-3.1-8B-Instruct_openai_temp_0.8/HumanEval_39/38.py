### Prime Fibonacci Generator

Below is a Python script that generates the n-th Fibonacci number that is also prime.

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
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
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.
    
    Args:
    n (int): The position of the prime Fibonacci number to return.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        num += 1


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

In this script, we first define a helper function `is_prime` to check if a number is prime. We then define the `fibonacci` function to generate the n-th Fibonacci number. The `prime_fib` function uses these two helper functions to find the n-th Fibonacci number that is also prime. The example usage at the end shows how to use the `prime_fib` function with different inputs.