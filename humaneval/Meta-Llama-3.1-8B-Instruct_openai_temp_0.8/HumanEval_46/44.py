### Fib4 Number Sequence Calculator
#### A Self-Contained Python Script

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
    
    Parameters:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The nth number in the Fib4 sequence.
    """
    if n <= 3:
        return [0, 0, 2, 0][n]
    
    fib4_sequence = [0, 0, 2, 0]
    
    for i in range(4, n + 1):
        next_number = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_number)
    
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that calculates the nth number in the Fib4 sequence. It uses an iterative approach to build up the sequence up to the nth number, then returns that number. The function includes a base case to handle the cases where n is 0, 1, 2, or 3, in which case the function returns a pre-computed value. The test cases at the end demonstrate that the function works as expected.