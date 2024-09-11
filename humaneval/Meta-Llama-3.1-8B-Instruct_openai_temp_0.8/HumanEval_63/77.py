```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the FibFib sequence.
    
    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 1
    
    fibfib_dict = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1}  # Precompute the first 5 elements
    
    for i in range(5, n + 1):
        fibfib_dict[i] = fibfib_dict[i - 1] + fibfib_dict[i - 2] + fibfib_dict[i - 3]
    
    return fibfib_dict[n]

# Test cases
print(fibfib(1))   # 0
print(fibfib(5))   # 4
print(fibfib(8))   # 24
```

However, if you want an even more efficient solution, you can use dynamic programming with a bottom-up approach and a list or dictionary to store the intermediate results. This will reduce the time complexity to O(n). Here's how you could implement it:

```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the FibFib sequence.
    
    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 2:
        return 0
    
    fibfib_list = [0] * (n + 1)  # Initialize the list to store the intermediate results
    fibfib_list[1] = 0
    fibfib_list[2] = 1
    fibfib_list[3] = 1
    
    # Fill up the list using the recurrence relation
    for i in range(4, n + 1):
        fibfib_list[i] = fibfib_list[i - 1] + fibfib_list[i - 2] + fibfib_list[i - 3]
    
    return fibfib_list[n]

# Test cases
print(fibfib(1))   # 0
print(fibfib(5))   # 4
print(fibfib(8))   # 24
```

This version of the function also includes test cases at the end to verify its correctness.