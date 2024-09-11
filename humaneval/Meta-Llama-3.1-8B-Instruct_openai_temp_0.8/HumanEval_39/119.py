```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
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
    fibonacci generates the n-th Fibonacci number.
    
    Args:
    n (int): The index of the Fibonacci number to generate.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number to check.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
        i += 1


# Example usage:
if __name__ == "__main__":
    n = 5
    result = prime_fib(n)
    print(f"The {n}-th Fibonacci number that is also prime is: {result}")
```

This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime by iterating up to the square root of the number.
2. `fibonacci(n)`: Generates the n-th Fibonacci number by recursively building the Fibonacci sequence.
3. `prime_fib(n)`: Finds the n-th Fibonacci number that is also prime by iteratively checking each Fibonacci number.

The example usage at the end demonstrates how to use the `prime_fib(n)` function to find the 5th Fibonacci number that is also prime.