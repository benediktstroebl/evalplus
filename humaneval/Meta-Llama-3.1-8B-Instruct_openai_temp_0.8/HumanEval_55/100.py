### Fibonacci Number Calculation
#### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
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

# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fib(i)}")
```

#### Explanation
This script uses a recursive approach to calculate the n-th Fibonacci number. However, this method is not efficient for large values of `n` because it performs many redundant calculations. A more efficient approach would use dynamic programming to store previously calculated Fibonacci numbers.

#### Hint for Efficiency Improvement
To improve the efficiency of the function for large values of `n`, you can use a bottom-up dynamic programming approach. The updated code would look something like this:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[n]

# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fib(i)}")
```