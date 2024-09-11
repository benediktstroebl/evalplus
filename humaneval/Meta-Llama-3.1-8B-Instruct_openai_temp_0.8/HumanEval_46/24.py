### Efficiently Computing the Fib4 Number Sequence
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

    This function efficiently computes the n-th element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize a list to store the first four fib4 numbers
        fib4_nums = [0, 0, 2, 0]
        
        # Compute the fib4 numbers iteratively
        for i in range(4, n + 1):
            # The ith fib4 number is the sum of the three preceding ones
            fib4_num = fib4_nums[i - 1] + fib4_nums[i - 2] + fib4_nums[i - 3] + fib4_nums[i - 4]
            fib4_nums.append(fib4_num)
        
        # Return the nth fib4 number
        return fib4_nums[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This Python script defines a function `fib4(n)` to efficiently compute the n-th element of the fib4 number sequence. It first checks for the base cases and then uses an iterative approach to compute the fib4 numbers. The script includes docstrings to provide a description of the function and its parameters, as well as example usage and test cases.