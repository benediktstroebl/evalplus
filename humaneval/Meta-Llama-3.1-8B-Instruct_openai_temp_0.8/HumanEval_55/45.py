### Fibonacci Number Calculation
#### Recursive and Iterative Solutions

```python
def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number using recursive approach.
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
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number using iterative approach.
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
    
    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr


def main():
    n = 10  # Change the value to calculate different Fibonacci numbers
    print(f"The {n}th Fibonacci number is:")
    print(f"Recursive approach: {fib_recursive(n)}")
    print(f"Iterative approach: {fib_iterative(n)}")


if __name__ == "__main__":
    main()
```

This script provides two functions to calculate the `n`-th Fibonacci number: `fib_recursive` uses a recursive approach, while `fib_iterative` uses an iterative approach. The `main` function demonstrates how to use these functions to calculate the 10th Fibonacci number using both approaches.

Note: Recursive approaches can be less efficient for large values of `n` due to the repeated function calls. The iterative approach is generally more efficient and preferred for large values of `n`.