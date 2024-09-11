### Fibonacci and Prime Function
#### prime_fib Function

Here is a Python function that solves the problem. This function uses the concept of a Fibonacci sequence and a helper function to check if a number is prime. 

```markdown
### Code
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
    n (int): The index of the number to return.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    a, b = 0, 1
    fib_index = 1
    while fib_index <= n:
        a, b = b, a + b
        if is_prime(b):
            fib_index += 1
            if fib_index == n:
                return b
    return "No such number found"


### Example Use Cases
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

### Explanation

The function `is_prime` checks if a number is prime by iterating from 2 to the square root of the number and verifying that it has no divisors. 

The function `prime_fib` uses the Fibonacci sequence to generate numbers and checks each number if it's prime using the `is_prime` function. It keeps track of the index of the Fibonacci numbers and stops when it finds the n-th number that is prime. 

This script will print the first n numbers in the Fibonacci sequence that are prime. If no such numbers are found, it will print "No such number found".