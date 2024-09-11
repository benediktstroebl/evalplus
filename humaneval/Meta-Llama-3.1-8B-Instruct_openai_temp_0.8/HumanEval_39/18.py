### Fibonacci and Prime Numbers
#### Python Script to Find the N-th Number that is Both a Fibonacci Number and a Prime Number

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


def fibonacci(num: int) -> int:
    """
    Generates the n-th Fibonacci number.

    Args:
        num (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.
    """
    if num <= 0:
        return "Input should be a positive integer."
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < num:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the number to find.

    Returns:
        int: The n-th number that is both a Fibonacci number and a prime number.
    """
    fib_index = 1
    while True:
        fib_num = fibonacci(fib_index)
        if is_prime(fib_num):
            if fib_index == n:
                return fib_num
            else:
                fib_index += 1
        else:
            fib_index += 1


# Test cases
if __name__ == "__main__":
    test_cases = {
        1: 2,
        2: 3,
        3: 5,
        4: 13,
        5: 89,
    }
    for n, expected_result in test_cases.items():
        result = prime_fib(n)
        print(f"prime_fib({n}) = {result}, Expected: {expected_result}")
        assert result == expected_result, f"Test case {n} failed"
    print("All test cases passed")
```
This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the n-th Fibonacci number, and `prime_fib` finds the n-th number that is both a Fibonacci number and a prime number. The script includes test cases to verify the correctness of the `prime_fib` function.