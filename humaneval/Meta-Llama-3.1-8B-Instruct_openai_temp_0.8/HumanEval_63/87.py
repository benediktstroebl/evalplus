```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        # Base case: fibfib(0) == 0 and fibfib(1) == 0
        return 0
    elif n == 2:
        # Base case: fibfib(2) == 1
        return 1
    else:
        # Initialize a list to store the computed FibFib numbers
        fibfib_nums = [0, 0, 1]
        
        # Compute the FibFib numbers up to the nth number
        for i in range(3, n + 1):
            # Compute the i-th FibFib number as the sum of the previous three numbers
            fibfib_num = fibfib_nums[i - 1] + fibfib_nums[i - 2] + fibfib_nums[i - 3]
            fibfib_nums.append(fibfib_num)
        
        # Return the nth FibFib number
        return fibfib_nums[n]


if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` to compute the nth element of the FibFib number sequence. It uses a bottom-up dynamic programming approach to efficiently compute the sequence. The function takes an integer `n` as input and returns the corresponding FibFib number. The script also includes test cases to verify the correctness of the function.