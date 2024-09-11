```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the Fib4 number to compute.

    Returns:
    int: The nth element of the Fib4 number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the Fib4 numbers
    fib4_numbers = [0, 0, 2, 0]
    
    # Compute the Fib4 numbers up to the nth number
    for i in range(4, n + 1):
        next_fib4 = fib4_numbers[i-1] + fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]
        fib4_numbers.append(next_fib4)
    
    # Return the nth Fib4 number
    return fib4_numbers[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses an iterative approach to compute the nth element of the Fib4 number sequence. It starts by storing the base cases in a list and then iteratively computes the remaining elements of the sequence up to the nth element. The nth element is then returned at the end of the function.