### Self-Contained Python Script
```markdown
### Fib4 Number Sequence
#### Efficiently Computing the n-th Element

The Fib4 number sequence is defined as follows:
- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

Here is an efficient Python function to compute the n-th element of the fib4 number sequence using dynamic programming:
```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Args:
    n (int): The index of the element to compute.
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n < 4:
        # Base cases
        return [0, 0, 2][n]
    
    # Initialize array to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0]*(n-3)
    
    # Compute the fib4 numbers iteratively
    for i in range(4, n+1):
        fib4_numbers[i-1] = fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]
    
    # Return the n-th element
    return fib4_numbers[n-1]

# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This function works by first checking the base cases (n < 4). It then initializes an array `fib4_numbers` to store the computed fib4 numbers. The function iteratively computes the fib4 numbers from 4 to n, using the recurrence relation `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. Finally, it returns the n-th element of the computed fib4 numbers.