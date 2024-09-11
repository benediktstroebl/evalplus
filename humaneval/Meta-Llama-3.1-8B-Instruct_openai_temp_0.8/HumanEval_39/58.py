### Fibonacci Prime Numbers
#### Python Script to Find the n-th Fibonacci Prime Number

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


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime number to find.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    fib_num = 1
    fib_next = 1
    fib_count = 1

    while fib_count < n:
        fib_next += fib_num
        fib_num, fib_next = fib_next, fib_num
        fib_count += 1

    while not is_prime(fib_num):
        fib_num -= 1
        while fib_num < fib_next:
            fib_next -= fib_num
            fib_num = (fib_num + fib_next) // 2

    return fib_num


# Test cases
def main():
    for i in range(1, 6):
        print(f"prime_fib({i}) = {fibonacci_prime(i)}")


if __name__ == "__main__":
    main()
```

This script defines two functions: `is_prime` to check if a number is prime and `fibonacci_prime` to find the n-th Fibonacci prime number. The `main` function tests the `fibonacci_prime` function with some test cases. The output will be the same as the provided docstring.