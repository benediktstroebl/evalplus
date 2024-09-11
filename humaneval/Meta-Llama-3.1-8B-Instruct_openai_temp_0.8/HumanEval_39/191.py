### Prime Fibonacci Numbers
#### Python Script

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


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number to check.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_count = 0
    num1, num2 = 0, 1
    while True:
        if is_prime(num1):
            fib_count += 1
            if fib_count == n:
                return num1
        num1, num2 = num2, num1 + num2


# Example usage
for i in range(1, 6):
    print(f"Prime Fibonacci number at position {i}: {prime_fib(i)}")
```

### Explanation

This Python script defines two functions: `is_prime` and `prime_fib`.

- The `is_prime` function checks if a given number is prime by iterating up to its square root and checking for divisibility.
- The `prime_fib` function generates Fibonacci numbers and checks if they are prime using the `is_prime` function. It returns the `n-th` prime Fibonacci number.

The example usage at the end prints the first five prime Fibonacci numbers.

### Time Complexity

The time complexity of the `is_prime` function is O(sqrt(n)), where n is the number being checked. The time complexity of the `prime_fib` function is O(n \* sqrt(m)), where n is the position of the Fibonacci number and m is the maximum Fibonacci number generated (which grows slowly). The overall time complexity is dominated by the `prime_fib` function for large n.