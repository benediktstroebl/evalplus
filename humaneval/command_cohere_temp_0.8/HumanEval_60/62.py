```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function uses the sum formula for the first n natural numbers, which is given by `n * (n + 1) // 2`. This formula is intuitively explained as follows:
1. `n` additions occur: `n + n + ... + n`  (n times).
2. `n + 1` additions occur in the first half and the second half, i.e., `n + n + 1 + 1 + ... + 1 + n` (n + 1 times).
3. The total sum is obtained by halving the sum of (1) and (2) above, i.e., `(n + n + 1 + ... + n) / 2`.

The total sum of integers from 1 to `N` is thus `N * (N + 1) // 2`. 

This code provides an efficient and accurate solution to the problem, and the unit tests confirm its correctness. You can integrate this code into a larger program or utilize it in a stand-alone capacity as and when required.