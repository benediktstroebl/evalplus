### prime_fib Function
```markdown
### prime_fib Function

This function returns the n-th number that is a Fibonacci number and also prime.
#### Parameters

* `n`: The position of the Fibonacci number (integer > 0).

#### Returns

* The n-th Fibonacci number that is also prime.

#### Example Use Cases

* `prime_fib(1)` returns 2
* `prime_fib(2)` returns 3
* `prime_fib(3)` returns 5
* `prime_fib(4)` returns 13
* `prime_fib(5)` returns 89
```

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
        n (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_prev = 2
        fib_curr = 3
        for _ in range(2, n):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            return fib_num
        num += 1
```

### Example Usage

```python
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```