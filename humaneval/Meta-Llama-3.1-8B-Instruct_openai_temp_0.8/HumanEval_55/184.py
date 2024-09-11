### Fibonacci Number Calculator
#### A Python Script to Calculate the N-th Fibonacci Number

Here is a Python script that implements the Fibonacci function using recursion and iteration.

```python
def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number using recursion.
    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number using iteration.
    >>> fib_iterative(10)
    55
    >>> fib_iterative(1)
    1
    >>> fib_iterative(8)
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


def main():
    n = int(input("Enter a number: "))
    print(f"Fibonacci number for {n} is: {fib_recursive(n)}")
    print(f"Fibonacci number for {n} (iterative) is: {fib_iterative(n)}")


if __name__ == "__main__":
    main()
```

This script defines two functions, `fib_recursive` and `fib_iterative`, to calculate the n-th Fibonacci number using recursion and iteration, respectively. The `main` function prompts the user to enter a number and then calls both functions to calculate and print the Fibonacci number.

### Note:
The recursive function has an exponential time complexity due to the repeated calculations of the same subproblems. The iterative function has a linear time complexity. The iterative function is generally more efficient for large values of `n`.