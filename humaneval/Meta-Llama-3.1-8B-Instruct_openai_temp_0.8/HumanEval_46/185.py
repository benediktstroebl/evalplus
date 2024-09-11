```python
def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Args:
    n (int): The position of the element in the fib4 sequence.
    
    Returns:
    int: The nth element of the fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    
    # Create a list to store the fib4 numbers, initializing it with the base cases
    fib4_numbers = [0] * (n + 1)
    fib4_numbers[0] = 0
    fib4_numbers[1] = 0
    
    # Calculate the fib4 numbers from 2 to n
    for i in range(2, n + 1):
        if i == 2:
            fib4_numbers[i] = 2
        elif i == 3:
            fib4_numbers[i] = 0
        else:
            fib4_numbers[i] = fib4_numbers[i - 1] + fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4]
    
    return fib4_numbers[n]
```

This function uses dynamic programming to store the computed fib4 numbers in a list, which allows it to efficiently compute the nth element by simply looking it up in the list.

You can test this function using the provided example use cases:
```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```