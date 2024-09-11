### Fib4 Number Sequence
#### Efficient Computation of the n-th Element
```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n <= 3:
        return {
            0: 0,
            1: 0,
            2: 2,
            3: 0
        }.get(n, None)  # Return default value if n is not in the dictionary

    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the next elements of the sequence
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d
```
This solution uses an iterative approach to compute the n-th element of the Fib4 number sequence. It initializes the first four elements of the sequence and then computes the next elements using a loop. The time complexity of this solution is O(n), which is more efficient than a recursive approach with a time complexity of O(2^n).