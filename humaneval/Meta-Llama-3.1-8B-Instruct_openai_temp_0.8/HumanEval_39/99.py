### Fibonacci Prime Numbers
#### Problem Description
Find the nth Fibonacci prime number.

#### Solution
```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_fib(n: int) -> int:
    """
    Returns the nth Fibonacci prime number.
    
    Args:
    n (int): The position of the Fibonacci prime number to find.
    
    Returns:
    int: The nth Fibonacci prime number.
    """
    count = 0
    num1, num2 = 2, 3
    while True:
        if is_prime(num1):
            count += 1
            if count == n:
                return num1
        num1, num2 = num2, num1 + num2


# Example usage
for i in range(1, 6):
    print(f"prime_fib({i}) = {prime_fib(i)}")
```
This script first defines a helper function `is_prime` to check if a number is prime. Then, it defines the main function `prime_fib` to find the nth Fibonacci prime number. The `prime_fib` function generates Fibonacci numbers and checks if they are prime using the `is_prime` function. The nth Fibonacci prime number is returned when the count of prime numbers reaches `n`.