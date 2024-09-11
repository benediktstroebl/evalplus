### Fib4 Number Sequence Calculator
#### Overview
This script calculates the nth element of the Fib4 number sequence using dynamic programming.

#### Code
```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the Fib4 number sequence to calculate.

    Returns:
        int: The nth element of the Fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the Fib4 numbers
    fib4_numbers = [0] * (n + 1)
    
    # Base cases
    fib4_numbers[0] = 0
    fib4_numbers[1] = 0
    fib4_numbers[2] = 2
    fib4_numbers[3] = 0
    
    # Calculate the rest of the Fib4 numbers using dynamic programming
    for i in range(4, n + 1):
        fib4_numbers[i] = fib4_numbers[i - 1] + fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4]
    
    # Return the nth Fib4 number
    return fib4_numbers[n]

# Test cases
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```

#### Explanation
This script uses dynamic programming to calculate the nth element of the Fib4 number sequence. It initializes a list to store the Fib4 numbers and uses a loop to calculate the rest of the numbers based on the previous four numbers in the sequence. This approach avoids the overhead of recursive function calls and makes the calculation more efficient for large values of n.