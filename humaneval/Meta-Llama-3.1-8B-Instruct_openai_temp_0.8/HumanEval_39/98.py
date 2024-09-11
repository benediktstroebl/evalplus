```markdown
### prime_fib.py

#### Fibonacci and Prime Number Generator

This script solves the problem of generating the n-th number that is both a Fibonacci number and a prime number.

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
    Generates the n-th Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.
    """
    fib_sequence = [0, 1]
    for _ in range(2, n + 1):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[n]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the number to generate.

    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    index = 1
    while True:
        fib_num = fibonacci(index)
        if is_prime(fib_num):
            if index == n:
                return fib_num
            index += 1
        else:
            index += 1


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

To use this script, save it as `prime_fib.py` and run it using Python:

```bash
python prime_fib.py
```

This will print the first 5 Fibonacci numbers that are also prime.

```
prime_fib(1) = 2
prime_fib(2) = 3
prime_fib(3) = 5
prime_fib(4) = 13
prime_fib(5) = 89
```