```python
def fibfib(n: int):
    """
    Compute the n-th element of the fibfib number sequence.

    The fibfib number sequence is a sequence similar to the Fibonacci sequence that's
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the fibfib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the computed values
        fibfib_values = [0, 0, 1] + [0] * (n - 2)
        
        # Compute the values iteratively
        for i in range(3, n + 1):
            fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]
        
        # Return the computed value
        return fibfib_values[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

However, this problem can be optimized by using a technique called memoization, which stores the results of expensive function calls and reuses them when the same inputs occur again. Here is the optimized solution using memoization:

```python
def fibfib(n: int, memo = {0: 0, 1: 0, 2: 1}):
    """
    Compute the n-th element of the fibfib number sequence.

    The fibfib number sequence is a sequence similar to the Fibonacci sequence that's
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.
        memo (dict): A dictionary to store the computed values.

    Returns:
        int: The n-th element of the fibfib number sequence.
    """
    if n not in memo:
        memo[n] = fibfib(n - 1, memo) + fibfib(n - 2, memo) + fibfib(n - 3, memo)
    
    # Return the computed value
    return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

In this optimized solution, a dictionary called `memo` is used to store the computed values. Before computing a value, the function checks if the value is already in the `memo` dictionary. If it is, the function returns the stored value instead of recomputing it. This avoids redundant computations and improves the performance of the function.