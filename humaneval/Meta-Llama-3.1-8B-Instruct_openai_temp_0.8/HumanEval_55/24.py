### Fibonacci Number Calculator

Here is a Python script that calculates the n-th Fibonacci number using a recursive function:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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

    # Base cases: F(1) = 1, F(2) = 1
    if n <= 1:
        return 1

    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fib(n-1) + fib(n-2)


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"F({i}) = {fib(i)}")
```

However, this recursive solution has an exponential time complexity due to repeated computation of the same Fibonacci numbers.

We can improve the solution by using a technique called "memoization" to store and reuse previously computed Fibonacci numbers.

### Optimized Fibonacci Number Calculator

Here is an optimized version of the Python script using memoization:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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
    memo = {0: 0, 1: 1}

    def fib_helper(k: int):
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    return fib_helper(n)


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"F({i}) = {fib(i)}")
```

Or even simpler using dynamic programming:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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
        return 1
    fib_list = [0] * (n + 1)
    fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"F({i}) = {fib(i)}")
```

All of these solutions have a linear time complexity of O(n), making them much more efficient than the recursive solution.