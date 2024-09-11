### Fibonacci Prime Generator

Here is a Python script that solves the problem:

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci_prime(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number to return.
    
    Returns:
    int: The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b


def main():
    n = int(input("Enter the position of the Fibonacci prime: "))
    print(f"The {n}-th Fibonacci prime number is {fibonacci_prime(n)}")


if __name__ == "__main__":
    main()
```

To run this script, save it in a file, for example, `fibonacci_prime.py`, then run it using `python fibonacci_prime.py`. When prompted, enter the position of the Fibonacci prime you're looking for. The script will print the result.

This script uses a simple iterative approach to generate Fibonacci numbers and checks each one for primality. The `is_prime` function checks if a number is prime by testing its divisibility up to its square root. The `fibonacci_prime` function keeps track of the count of prime Fibonacci numbers found so far and returns the n-th one when the count reaches n.