```python
def memoized_fibfib(n: int, memo: dict = {}) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence 
    using memoization to store previously computed values.
    
    :param n: The index of the element in the fibfib sequence to be computed.
    :param memo: A dictionary to store previously computed values.
    :return: The n-th element of the fibfib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = memoized_fibfib(n-1, memo) + memoized_fibfib(n-2, memo) + memoized_fibfib(n-3, memo)
        return memo[n]


def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    :param n: The index of the element in the fibfib sequence to be computed.
    :return: The n-th element of the fibfib sequence.
    """
    return memoized_fibfib(n)


# Test the function
print(fibfib(1))    # 0
print(fibfib(5))    # 4
print(fibfib(8))    # 24
```

This script defines a `memoized_fibfib` function that uses a dictionary to store previously computed values, and a `fibfib` function that wraps it. The `memoized_fibfib` function uses recursion to compute the n-th element of the fibfib sequence, while the `fibfib` function provides a simple interface to it. The script also includes test cases to verify the correctness of the implementation.