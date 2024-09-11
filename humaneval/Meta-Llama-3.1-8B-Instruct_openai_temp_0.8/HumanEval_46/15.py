```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n: The index of the Fibonacci number to compute.

    Returns:
        The nth Fibonacci number.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the Fibonacci numbers
    fib4_sequence = [0, 0, 2, 0]
    
    # Compute the Fibonacci numbers up to the nth number
    for i in range(4, n + 1):
        # The next number is the sum of the previous four numbers
        next_number = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_number)
    
    # Return the nth Fibonacci number
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```
This script defines the function `fib4(n)` to compute the nth Fibonacci number. It uses a loop to build up the Fibonacci sequence iteratively, similar to the way a recursive function would be implemented, but without the overhead of recursive function calls. The function includes a simple test at the end to verify that it produces the correct results for the given test cases.