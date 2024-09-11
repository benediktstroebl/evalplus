### Fibonacci Number Calculator
#### Problem: Calculate the n-th Fibonacci Number

A Fibonacci number is a number in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on, in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

#### Solution
```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n == 0:  # Base case: 0th Fibonacci number is 0
        return 0
    elif n == 1:  # Base case: 1st Fibonacci number is 1
        return 1
    else:  # Recursive case: Calculate n-th Fibonacci number as sum of (n-1)th and (n-2)th
        return fib(n-1) + fib(n-2)

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
#### Explanation

This script uses a recursive approach to calculate the n-th Fibonacci number. The base cases are when `n` is 0 or 1, in which case we return 0 and 1, respectively. For any other value of `n`, we recursively calculate the n-th Fibonacci number as the sum of the (n-1)th and (n-2)th Fibonacci numbers.

Please note that this recursive approach can be inefficient for large values of `n` due to repeated calculations. A more efficient approach would be to use dynamic programming or an iterative method.