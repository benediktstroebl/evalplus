### Fibonacci Number Calculator
#### Recursive Solution
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13,...

    :param n: The index of the Fibonacci number to be calculated.
    :return: The n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Example usage:
print(fib(10))   # Output: 55
print(fib(1))    # Output: 1
print(fib(8))    # Output: 21
```
This recursive function calculates the n-th Fibonacci number by calling itself with the arguments `n-1` and `n-2` and summing their results.

However, the above recursive Fibonacci function has an exponential time complexity, which becomes inefficient for large inputs.

#### Iterative Solution
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    :param n: The index of the Fibonacci number to be calculated.
    :return: The n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


# Example usage:
print(fib(10))   # Output: 55
print(fib(1))    # Output: 1
print(fib(8))    # Output: 21
```
This iterative function uses a loop to calculate the n-th Fibonacci number, which has a linear time complexity and is more efficient for large inputs.