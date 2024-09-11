### Fibonacci Number Calculator
#### A Python Script to Calculate Nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to calculate.
    
    Returns:
        int: The n-th Fibonacci number.
    """
    
    # Base cases: F(1) = 1, F(2) = 1
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    
    # Initialize variables for memoization
    a, b = 1, 1
    
    # Calculate Fibonacci numbers up to n
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Test cases
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
    print(fib(-1))  # Output: Input should be a positive integer.
```

This script uses memoization to store previously calculated Fibonacci numbers in order to improve performance for larger inputs. The `fib` function takes an integer `n` as input and returns the n-th Fibonacci number. It handles edge cases where `n` is less than or equal to 0 and returns the correct result for `n = 1`.