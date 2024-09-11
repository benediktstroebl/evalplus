### Prime Fibonacci Number Generator

The following Python script generates the `n-th` prime Fibonacci number.

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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_perfect_square(num: int) -> bool:
    """
    Checks if a number is a perfect square.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    return num >= 0 and (num ** 0.5) % 1 == 0


def nth_fibonacci(n: int) -> int:
    """
    Calculates the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    fib_sequence = [0, 1]
    if n == 1:
        return fib_sequence[0]
    elif n == 2:
        return fib_sequence[1]
    else:
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th prime Fibonacci number.

    Args:
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 1
    i = 1
    while True:
        fibonacci_num = nth_fibonacci(i)
        if is_prime(fibonacci_num):
            count += 1
            if count == n:
                return fibonacci_num
        i += 1


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"Fibonacci number {i} that is prime is: {prime_fib(i)}")
```

This script defines four functions: `is_prime`, `is_perfect_square`, `nth_fibonacci`, and `prime_fib`. The `prime_fib` function uses a loop to generate Fibonacci numbers and checks each one to see if it is prime, returning the `n-th` prime Fibonacci number when the loop is finished.