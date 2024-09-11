### Fibonacci Number Generator
#### Recursive and Iterative Solutions

Here's a Python script that defines a function `fib` to calculate the `n`-th Fibonacci number using both recursive and iterative approaches.

```markdown
### Code
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
    return fib_recursive(n-1) + fib_recursive(n-2)


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


# Example usage:
if __name__ == "__main__":
    num_fib = 10  # Change this to calculate a different Fibonacci number
    print(f"The {num_fib}th Fibonacci number is:")
    print(f"Recursive solution: {fib_recursive(num_fib)}")
    print(f"Iterative solution: {fib_iterative(num_fib)}")
```
#### Explanation

* The `fib_recursive` function uses recursion to calculate the `n`-th Fibonacci number. It works by calling itself to calculate the `(n-1)`th and `(n-2)`th Fibonacci numbers and then adding them together.
* The `fib_iterative` function uses iteration to calculate the `n`-th Fibonacci number. It initializes two variables, `fib_prev` and `fib_curr`, to the first two Fibonacci numbers (0 and 1). It then enters a loop that runs from `2` to `n`, updating the Fibonacci numbers in each iteration.
* In the example usage section, we calculate the 10th Fibonacci number using both the recursive and iterative solutions and print the results.
* Note that the recursive solution has a higher time complexity (O(2^n)) compared to the iterative solution (O(n)), making the iterative solution more efficient for large values of `n`.