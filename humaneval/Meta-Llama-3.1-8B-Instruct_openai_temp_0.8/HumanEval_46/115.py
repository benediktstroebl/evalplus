### Fib4 Number Sequence Generation
#### Problem Description

The `fib4` function calculates the `n-th` element of the fib4 number sequence, which is defined as:

* `fib4(0)` -> 0
* `fib4(1)` -> 0
* `fib4(2)` -> 2
* `fib4(n)` -> `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)`

#### Solution

```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the fib4 number sequence.

    Example:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 2:  # Base cases
        return 0 if n <= 1 else 2
    elif n == 3:  # Another base case
        return 0
    else:
        # Initialize the first four elements
        a, b, c, d = 0, 0, 2, 0
        
        # Compute the rest of the sequence
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c + d
        
        # Return the n-th element
        return d
```

This solution uses an iterative approach to calculate the fib4 number sequence, storing the last four elements in variables `a`, `b`, `c`, and `d`. This approach has a time complexity of O(n), which is more efficient than a recursive solution for large values of `n`.