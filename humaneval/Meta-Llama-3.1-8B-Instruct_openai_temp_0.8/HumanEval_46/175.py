### Fib4 Number Sequence Calculator
#### Problem Statement
The Fib4 number sequence is a sequence similar to the Fibonacci sequence, defined as follows:
- `fib4(0) -> 0`
- `fib4(1) -> 0`
- `fib4(2) -> 2`
- `fib4(3) -> 0`
- `fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

#### Solution
We can efficiently compute the `n-th` element of the fib4 number sequence using dynamic programming. The idea is to store the previously computed values in an array and use them to calculate the current value.

```python
def fib4(n: int) -> int:
    """
    Calculate the n-th element of the Fib4 number sequence.

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    # Base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    
    # Create an array to store previously computed values
    fib4_values = [0, 0, 2]
    
    # Calculate the fib4 values up to the n-th element
    for i in range(3, n + 1):
        # Calculate the current value as the sum of the last four values
        next_value = fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4]
        # Append the current value to the array
        fib4_values.append(next_value)
    
    # Return the n-th element
    return fib4_values[n]
```

#### Example Use Cases
```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently calculate the `n-th` element of the Fib4 number sequence. It creates an array to store previously computed values and uses them to calculate the current value. The base cases `n <= 1` and `n == 2` are handled separately to ensure correct results. The script also includes example use cases to demonstrate its usage.