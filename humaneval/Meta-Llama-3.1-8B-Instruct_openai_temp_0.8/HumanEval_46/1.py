### Fib4 Number Sequence
#### Python Implementation
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the Fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the array to store the sequence
        fib4_sequence = [0, 0, 2]
        
        # Compute the sequence up to the nth number
        for i in range(3, n + 1):
            next_number = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
            fib4_sequence.append(next_number)
        
        # Return the nth number in the sequence
        return fib4_sequence[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```
This script uses an iterative approach to compute the nth number in the Fib4 sequence, avoiding recursion for efficiency. It initializes an array with the base cases and then computes each subsequent number in the sequence. The nth number is then returned.