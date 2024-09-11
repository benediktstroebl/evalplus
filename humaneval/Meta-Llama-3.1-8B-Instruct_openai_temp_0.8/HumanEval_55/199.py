### Fibonacci Number Generator
#### Recursive Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Test cases
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci number at position {n}: {fib(n)}")
```

This script uses a recursive approach to calculate the n-th Fibonacci number, which is the sum of the two preceding numbers in the sequence. However, please note that this recursive solution is not efficient for large values of `n` due to repeated calculations. A more efficient solution would involve memoization or an iterative approach.

### Iterative Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n]

# Test cases
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci number at position {n}: {fib(n)}")
```

This iterative solution has a time complexity of O(n) and is more efficient for large values of `n`. It uses a list to store the Fibonacci sequence up to the n-th number, and then returns the n-th number.