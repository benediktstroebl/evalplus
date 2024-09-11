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
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(num**0.5) + 1
    for d in range(3, max_divisor, 2):
        if num % d == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    count = 1
    num = 1
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```
This script defines a function `prime_fib(n)` which generates the nth Fibonacci number that is also prime. It uses the helper functions `is_prime(num)` to check if a number is prime and `fibonacci(n)` to generate the nth Fibonacci number. The script also includes example usage at the end to demonstrate how to use the `prime_fib(n)` function.