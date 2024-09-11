```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    This function uses dynamic programming to calculate the n-th Fibonacci number efficiently.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    
    # Create a list to store Fibonacci numbers
    fib_nums = [0, 1]
    
    # Generate Fibonacci numbers up to n
    for i in range(2, n + 1):
        # Calculate the next Fibonacci number as the sum of the previous two
        next_num = fib_nums[i - 1] + fib_nums[i - 2]
        fib_nums.append(next_num)
    
    # Return the n-th Fibonacci number
    return fib_nums[n]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a `fib` function that calculates the n-th Fibonacci number using dynamic programming. It creates a list to store Fibonacci numbers and then generates them iteratively, storing the result in the list. Finally, it returns the n-th Fibonacci number from the list. The script also includes example usage at the end to demonstrate how to use the `fib` function.