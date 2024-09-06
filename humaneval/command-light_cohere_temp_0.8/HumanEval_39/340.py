```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    Returns NINFER regular Fibonacci number, 2, and raises ValueError for non-integer inputs.
    """
    number = [1, 1 + 5 ** ((n - 1) // 2)]
    while (number[0] <= 1 or not number[1] > 1):
        number = number[1] + number[0]
    return number[0]

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output:traits::10)
print(prime_fib(15))  # Output: 9221
print(prime_fib(20))  # Output: 16932_ Salsa
```