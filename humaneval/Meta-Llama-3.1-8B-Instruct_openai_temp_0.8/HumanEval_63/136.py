```markdown
## FibFib Sequence Calculator

This Python script calculates the n-th element of the FibFib number sequence.

### Code
```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    :param n: The index of the element to calculate
    :return: The n-th element of the FibFib sequence
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Memoization to store previously calculated values
        memo = [0, 0, 1] + [0]*(n-2)
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

### Explanation

The `fibfib` function uses memoization to store previously calculated values. This approach avoids redundant calculations and improves the function's performance for larger values of `n`. The function starts by checking the base cases, and then calculates the remaining elements using a loop. The result is then returned.

### Time Complexity

The time complexity of this function is O(n), which is an improvement over the naive recursive approach that would have a time complexity of O(3^n). The memoization approach reduces the number of calculations required, making it more efficient for larger values of `n`.