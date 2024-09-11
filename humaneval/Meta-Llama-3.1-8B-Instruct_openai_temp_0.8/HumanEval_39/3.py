### Prime Fibonacci Numbers
#### Python Script
```markdown
### prime_fib.py

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
    if n <= 1:
        return n
    fib = [0, 1]
    for _ in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Testing complete.")
```

### Usage
To run the script and test the functions, save it to a file (e.g., `prime_fib.py`) and execute it using Python:

```bash
python prime_fib.py
```
This will run the doctests and print "Testing complete." if they pass.
```