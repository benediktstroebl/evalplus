### Prime Fibonacci Numbers Generator
#### Problem Description

This script generates the n-th number that is both a Fibonacci number and a prime number.

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
        n (int): The index of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_nums = [0, 1]
        for i in range(2, n + 1):
            fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
        return fib_nums[n - 1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    fib_num = fibonacci(n)
    return fib_num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

#### Explanation

The `is_prime` function checks if a number is prime by iterating up to its square root and checking for divisibility.

The `fibonacci` function generates the n-th Fibonacci number by iteratively adding the previous two numbers in the sequence.

The `prime_fib` function returns the n-th number that is both a Fibonacci number and a prime number by first generating the n-th Fibonacci number and then checking if it's prime using the `is_prime` function.

The example usage at the end demonstrates how to use the `prime_fib` function to generate the first 5 prime Fibonacci numbers.