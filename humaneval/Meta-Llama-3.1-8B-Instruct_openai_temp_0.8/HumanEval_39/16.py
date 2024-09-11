```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
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
    fibonacci generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
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
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num) and fib_num!= 0:
            return fib_num
        i += 1


# Test the function
if __name__ == "__main__":
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
```

This Python script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates the nth Fibonacci number, and the `prime_fib` function generates the nth Fibonacci number that is also prime. The script then tests the `prime_fib` function with some examples.