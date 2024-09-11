```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition
    of the last two numbers, starting with 0 and 1.

    For n = 1, fib(n) = 1
    For n > 1, fib(n) = fib(n-1) + fib(n-2)

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

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
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fib({i}) = {fib(i)}")
```

However, please note that this recursive implementation of the Fibonacci function is not efficient for large inputs. This is because it does a lot of repeated work, calculating the same subproblems over and over. A more efficient solution would use dynamic programming, memoizing the results of subproblems to avoid recalculating them.

Here is an improved version of the function:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}
    def fib_helper(k):
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    return fib_helper(n)


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fib({i}) = {fib(i)}")
```

Or, even more efficient, using matrix exponentiation:

```python
def multiply(F, M):
    x = F[0][0]*M[0][0] + F[0][1]*M[1][0]
    y = F[0][0]*M[0][1] + F[0][1]*M[1][1]
    z = F[1][0]*M[0][0] + F[1][1]*M[1][0]
    w = F[1][0]*M[0][1] + F[1][1]*M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1,1],
         [1,0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2!= 0:
        multiply(F, M)

def fib(n):
    F = [[1,1],
         [1,0]]

    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

# Example usage:
if __name__ == "__main__":
    for i in range(1