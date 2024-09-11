### **FibFib Number Sequence**
### **Efficient Python Implementation**

```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is defined as follows:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element in the sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_values = [0] * (n + 1)
        fibfib_values[0] = 0
        fibfib_values[1] = 0
        fibfib_values[2] = 1
        for i in range(3, n + 1):
            fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
        return fibfib_values[n]

# Example usage
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

In this solution, we use dynamic programming to store the previously computed values in a list `fibfib_values`. We initialize the list with `n + 1` zeros and then fill it up iteratively using a loop. This approach reduces the time complexity from O(2^n) to O(n), making the function much more efficient for large values of `n`.