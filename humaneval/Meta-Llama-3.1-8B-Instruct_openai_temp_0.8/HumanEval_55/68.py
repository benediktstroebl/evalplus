### Fibonacci Number Generator
#### Recursive and Iterative Solutions

Below is a Python script that includes both recursive and iterative solutions to calculate the nth Fibonacci number.

```python
def fib_recursive(n: int) -> int:
    """
    Recursive function to calculate the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Iterative function to calculate the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b

    return b


# Example usage:
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci({n}) = {fib_recursive(n)}")
        print(f"Fibonacci({n}) = {fib_iterative(n)}")
```

The `fib_recursive` function uses a recursive approach, while the `fib_iterative` function uses an iterative loop to calculate the nth Fibonacci number. Both functions are well-documented and include example usage in the script.

**Optimization Note:**
The iterative solution (`fib_iterative`) is generally more efficient than the recursive solution (`fib_recursive`) for large values of `n`, as it avoids the overhead of recursive function calls. However, both solutions have a time complexity of O(n) and a space complexity of O(1), making them suitable for calculating large Fibonacci numbers.